$(document).ready(function () {
    $.get('/get_product_names', function (productNames) {
       var availableTags = productNames;
        $("#tags").autocomplete({
          source: availableTags
        });
    });

    $.get('/get_product_names', function (productNames) {
       var availableTags = productNames;
        $(".autocomplete").autocomplete({
          source: availableTags
        });
    });
});
