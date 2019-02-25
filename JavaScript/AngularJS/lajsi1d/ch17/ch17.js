var app = angular.module("app", []);

app.controller("MainCtrl", function ($scope) {
  $scope.message = "Chapter 17: Tables";

  $scope.guitarists = [
    {
      name: "Eddie Van Halen",
      song: "Eruption",
      technique: "tapping"
    },
    {
      name: "Eric Johnson",
      song: "East Wes",
      technique: "harp harmonics"
    },
    {
      name: "Joe Satriani",
      song: "Ice #9",
      technique: "whammy bar lizard slide"
    },
    {
      name: "Santana",
      song: "Black Magic Woman",
      technique: "supernatural slide bend"
    },
    {
      name: "Jimi Hendrix",
      song: "All Along the Watchtower",
      technique: "voodoo unison bend"
    },
    {
      name: "Yngwie Malmsteen",
      song: "Black Star",
      technique: "neoclassical sweep picking"
    },
    {
      name: "Steve Vai",
      song: "For the Love of God",
      technique: "bee telepathy"
    }
  ];

});

