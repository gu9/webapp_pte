$(document).on('ready', function() {
    "use strict";

    
    if ($("#navigation, #navigation-regular, #navigation-transparent").length) {

			$("#navigation, #navigation-regular, #navigation-transparent").menumaker({
		        title: "Menu",
		        format: "multitoggle"
		    });

    }

    if ($('.video').length) {

    $('.video').magnificPopup({
          type: 'iframe',


          iframe: {
              markup: '<div class="mfp-iframe-scaler">' +
                  '<div class="mfp-close"></div>' +
                  '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>' +
                  '<div class="mfp-title">Some caption</div>' +
                  '</div>'
          },
          callbacks: {
              markupParse: function(template, values, item) {
                  values.title = item.el.attr('title');
              }
          }


      });

	}


});


