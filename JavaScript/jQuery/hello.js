// jQuery gets imported by the HTML file.
// You can do it from a JavaScript file, but it isn't as concise.

// Register a click event handler for a button.
// When clicked, the CSS class "big" is added to the paragraph.
$("button#enlarge").on("click", function () {
	$("p#alice").addClass("big");
});

// Register a click event handler for a button.
// When clicked, the CSS class "big" is removed from the paragraph.
$("button#reduce").on("click", function () {
	$("p#alice").removeClass("big");
});

// Toggle visibility of the logo image when this button is pressed.
$("button#toggle").on("click", function () {
	$("img#logo").toggle("slow");
});



