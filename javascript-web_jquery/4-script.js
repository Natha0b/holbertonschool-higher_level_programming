const classes = ['red', 'green'];
$('#toggle_header').addClass(classes[Math.floor(Math.random() * classes.length)]);
$('#toggle_header').on('click', () => {
  if ($(this).hasClass('red')) {
    $(this).addClass('green');
    $(this).removeClass('red');
  } else if ($(this).hasClass('green')) {
    $(this).addClass('red');
    $(this).removeClass('green');
  }
});
