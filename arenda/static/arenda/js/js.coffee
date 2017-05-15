$().ready ->
    $("div.content").on("click", ".filter a, .wrap-paginate a", (e) ->
        e.preventDefault()

        $("div.content").load $(this).attr("href")
    )

    $contactForm = $("div.contact-form")

    $contactForm.on("submit", "form", (e) ->
        e.preventDefault()

        $form = $(this);
        contactUrl = $form.attr("action");
        data = $form.serializeArray();

        $contactForm.load(contactUrl, data, ->
            $("ul.errorlist").each(->
                $span = $(this).parent()
                fieldName = $span.data("field")

                if fieldName != "__all__"
                    $field = $contactForm.find("[name=#{fieldName}]")
                    $field.addClass("error-field")
            )
        )
    )

    $("ul.image-gallery").lightSlider
        gallery: true
        item: 1
        slideMargin: 0
        loop: true
        enableDrag: false
        thumbItem: 9

        onSliderLoad: (e) ->
            e.lightGallery
                selector: "ul.image-gallery .lslide"
