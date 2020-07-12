<?php 

include "Movie.php";

class AwardWinningMovie extends Movie{

    private $award;

    public function __construct($pId, $pTitle, $pRentalPrice, $pAward){
        parent::__construct($pId, $pTitle, $pRentalPrice); 
        $this->award = $pAward;
    } 
    
    public function recommend($country){

        switch ($this->award){
            case 'Best Picture':
                $others = 'The Rail';
                break;
            case 'Best Actor':
                $others = '1729';
                break;
            default:
                $others = 'And so it begins';
        }

        return
            'You might also like:<BR>'.
            '<BR>Movie Title = '.$others.
            '<BR>Rental Price = '.$this->conversion($country);
    } 
    
/*    
    public function displayHeading($tag){
        $baseMsg = parent::displayHeading($tag);
        return $baseMsg.$this->award;
    }
    
*/    
} 
