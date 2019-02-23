var app = angular.module("app", []);

// Technically, we're defining a controller type and providing its constructor function.
// So, the type name should be uppercase.
app.controller("MainCtrl", function ($scope) {
    // The scope is the view model.
    // AngularJS provides two-way data binding between the scope and the view (DOM elements).
    $scope.message = "This is chapter 5.";

    // Make a list of TurboGrafx 16 games to loop over with ng-repeat.
    $scope.games = [
        "Military Madness",
        "Bonk's Adventure",
        "Dungeon Explorer",
        "Ys Book I & II",
        "Fighting Street",
        "R-Type",
        "The Legendary Axe",
        "China Warrior",
        "Ninja Spirit",
        "Blazing Lazers",
        "Devil's Crush",
        "Keith Courage in the Alpha Zones",
        "Space Harrier",
        "Splatterhouse"
    ];

    $scope.ceos = [
        { name: "Jeff Bezos", company: "Amazon" },
        { name: "Elon Musk", company: "Tesla" },
        { name: "Bill McDermott", company: "SAP" },
        { name: "Ryan Smith", company: "Qualtrics" }
    ]
});
