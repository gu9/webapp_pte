  $(document).ready(function() {
      "use strict";
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
  })