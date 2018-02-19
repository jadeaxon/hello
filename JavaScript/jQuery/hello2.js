// jQuery gets imported by the HTML file.
// You can do it from a JavaScript file, but it isn't as concise.

// Handles form submission.  Displays personalized greeting in heading below it.
$("form#userName").on("submit", function () {
  var first_name = $("input#firstName").val();
  var last_name = $("input#lastName").val();
  $("h4#greeting").text("Hello, " + first_name + " " + last_name + "!");
});

// Boosts the users ego by applying style to the greeting.
$("button#ego").on("click", function () {
  $("h4#greeting").addClass("ego");
});


