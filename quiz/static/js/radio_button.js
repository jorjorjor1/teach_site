var check;

$('input[type="radio"]').hover(function() {
    check = $(this).is(':checked');
});

$('input[type="radio"]').click(function() {
    check = !check;
    $(this).attr("checked", check);
});