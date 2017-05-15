from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import Place, Kind


class PlaceList(ListView):
    model = Place

    paginate_by = 8

    def dispatch(self, request, *args, **kwargs):
        if 'filter' not in request.session:
            request.session['filter'] = [str(x) for x in Kind.objects.values_list('id', flat=True)]

        if request.is_ajax():
            self.template_name = 'arenda/_place_list.html'
        else:
            self.template_name = 'arenda/place_list.html'

        if 'kind_id' in kwargs:
            if 'page' in request.session:
                del request.session['page']

            kind_id = kwargs['kind_id']

            if kind_id in request.session['filter']:
                request.session['filter'].remove(kind_id)
            else:
                request.session['filter'].append(kind_id)

            request.session.save()

        if 'page' in kwargs:
            request.session['page'] = int(kwargs['page'])
            request.session.save()
        elif 'page' in request.session:
            self.kwargs['page'] = request.session['page']

        return super(PlaceList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Place.objects.filter(kinds__in=self.request.session['filter'])

    def get_context_data(self, **kwargs):
        context = super(PlaceList, self).get_context_data(**kwargs)
        context['kind_list'] = Kind.objects.all()

        return context


class PlaceDetail(DetailView):
    model = Place


class About(TemplateView):
    template_name = 'arenda/about.html'


class Contact(FormView):
    form_class = ContactForm

    template_name = 'arenda/contact.html'
    success_url = '/contact/'

    def get_context_data(self, **kwargs):
        context = super(Contact, self).get_context_data()
        context['yandex_um'] = settings.YANDEX_UM

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = self.get_form()

        if form.is_valid():
            sender = form.cleaned_data['sender']
            phone = form.cleaned_data['phone']
            mail = form.cleaned_data['mail']
            message = form.cleaned_data['message']

            full_message = 'Отправитель: %s\n' \
                           'Телефон: %s\n' \
                           'E-mail: %s\n' \
                           'Сообщение: \n %s' % (sender, phone, mail, message)

            try:
                send_mail('Сообщение из формы обратной связи',
                          full_message,
                          settings.EMAIL_SENDER,
                          settings.EMAIL_COPY_TO
                          )

                if mail:
                    send_mail('Подтверждение о доставке',
                              full_message,
                              settings.EMAIL_SENDER,
                              [mail]
                              )

            except Exception as e:
                context['form'].add_error(None, 'При отправке произошла ошибка')

            else:
                context['form'] = self.get_form_class()
                context['successful_send'] = True

        if request.is_ajax():
            template_name = 'arenda/_contact_form.html'
        else:
            template_name = 'arenda/contact.html'

        return render(request, template_name, context)
