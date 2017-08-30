$(document).ready(function () {

    var products = [];

    $('#add_btn').on('click', function () {
        var productName = $('#well-input-product').val(),
            productWeight = $('#well-input-product-weight').val(),
            row = '<tr><td>'+ productName +'</td><td>' + productWeight + '</td></tr>';
        $('#products > tbody:last-child').append(row);
        products.push([productName, productWeight]);
    });

    $('#submit_btn').on('click', function () {
        var weight = $('#weight').val();
        if (weight && products.length > 0) {
            $.ajax({
                data: JSON.stringify({
                    'weight': weight,
                    'products': products
                }),
                type: 'POST',
                url: '/calculate',
                contentType: 'application/json',
                dataType: 'json'
            }).done(function (data) {
                var proteinCompleteClass = data['need']['protein'] - data['got']['protein'] < 0 ? 'success': 'danger',
                    fatCompleteClass = data['need']['fat'] - data['got']['fat'] < 0 ? 'success': 'danger',
                    carbohydrateCompleteClass = data['need']['carbohydrate'] - data['got']['carbohydrate'] < 0 ? 'success': 'danger';

                var proteinComplete = data['need']['protein'] - data['got']['protein'] < 0 ? 'yes': 'no',
                    fatComplete = data['need']['fat'] - data['got']['fat'] < 0 ? 'yes': 'no',
                    carbohydrateComplete = data['need']['carbohydrate'] - data['got']['carbohydrate'] < 0 ? 'yes': 'no';

                    table = "<table class=\"table table-bordered table-striped\">\n" +
                    "            <thead>\n" +
                    "              <tr>\n" +
                    "                <th>Nutrients</th>\n" +
                    "                <th>Need (gram)</th>\n" +
                    "                <th>Eaten (gram)</th>\n" +
                    "                <th>Complete</th>\n" +
                    "              </tr>\n" +
                    "            </thead>\n" +
                    "            <tbody>\n" +
                    "              <tr class="+ proteinCompleteClass +">\n" +
                    "                <td>protein</td>\n" +
                    "                <td>"+ data['need']['protein'] +"</td>\n" +
                    "                <td>"+ data['got']['protein'] +"</td>\n" +
                    "                <td>"+ proteinComplete +"</td>\n" +
                    "              </tr>\n" +
                    "              <tr class="+ fatCompleteClass +">\n" +
                    "                <td>fat</td>\n" +
                    "                <td>"+ data['need']['fat'] +"</td>\n" +
                    "                <td>"+ data['got']['fat'] +"</td>\n" +
                    "                <td>"+ fatComplete +"</td>\n" +
                    "              </tr>\n" +
                    "              <tr class="+ carbohydrateCompleteClass +">\n" +
                    "                <td>carbohydrate</td>\n" +
                    "                <td>"+ data['need']['carbohydrate'] +"</td>\n" +
                    "                <td>"+ data['got']['carbohydrate'] +"</td>\n" +
                    "                <td>"+ carbohydrateComplete +"</td>\n" +
                    "              </tr>\n" +
                    "            </tbody>\n" +
                    "        </table>";
                $('.result-table').append(table).hide().fadeIn('slow');
            });
        }
        else if (!weight)
            alert('Set your weight.');
        else if (products.length === 0)
            alert('You don\'t have add any products.')
    });
});