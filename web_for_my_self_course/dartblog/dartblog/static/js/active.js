$(document).ready(function () {

    const filterFns = {
        numberGreaterThan50: function () {
            const number = $(this).find('.number').text();
            return parseInt(number, 10) > 50;
        },
        ium: function () {
            const name = $(this).find('.name').text();
            return name.match(/ium$/);
        }
    };

    $('.menu a').each(function () {
        let location = window.location.protocol + '//' + window.location.host + window.location.pathname;
        let link = this.href;
        if (location === link) {
            $(this).parent().addClass('active');
        }
    });

    $('.filters-button-group').on('click', 'button', function () {
        let filterValue = $(this).attr('data-filter');
        filterValue = filterFns[filterValue] || filterValue;
        $grid.isotope({
            filter: filterValue
        });
    });
    $('.button-group').each(function (i, buttonGroup) {
        const $buttonGroup = $(buttonGroup);
        $buttonGroup.on('click', 'button', function () {
            $buttonGroup.find('.is-checked').removeClass('is-checked');
            $(this).addClass('is-checked');
        });
    });
});