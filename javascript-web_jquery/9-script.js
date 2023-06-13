$(document).ready(function () {
  const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.getJSON(URL, function (data) {
    const hello = data.hello;
    $('DIV#hello').text(hello);
  });
});
