/*
 title: Embedded system
 Author: tomzx
 Template: page
 Permalink: /portfolio/embedded-system/
*/
**Description**  
The goal of this embedded system, which was mounted on a 2 wheels, 2 ball-bearing base, was to accomplish a series of tasks. More specifically:

*   Navigate a grid based map, following black duct tape assembled in a grid fashion
*   Go from a point A to a point B on the grid which has the duct tape line (director) removed
*   Detect magnets at every grid position and then solve the 8 queens problem (using the detected magnets as queens positions)
*   Avoid a wall place on an adjacent row of the grid, using distance detector to tell if there's a hole in the wall we can go through
*   Avoid a post on a certain grid coordinate, using distance detector
*   Do rotations at a specific location, rotating at a specific angular velocity based on the proximity of a hand from the detector. Robot had to detect its grid orientation

This robot was using the following sensors/outputs to accomplish those tasks:

*   Infrared detector
*   LCD display
*   Status LED
*   Lynx Motion (line detector)
*   Magnetic field sensor
*   Motors
*   Sonar
*   Piezo electric sound emitter
</u>

**Snippet**

<pre><code class="language-cpp line-numbers">/*!
 * \brief La classe principale qui se charge des différents périphériques.
 */
class Robot{
public:
    //! Pointeur vers l'instance actuelle du robot
    static Robot* instance_;
    //! État du reset
    static bool reset;
    
    //! Constructeur
    Robot();
    //! Obtenir l'instance du robot
    static Robot* getInstance();
    //! Destructeur
    ~Robot();
    
    //! Initier le robot
    void init();
    //! Réinitialiser le robot (soft reset)
    void resetRobot();
    //! Boucle infinie principale
    void fonctionner();
    //! S'occupe d'envoyer le robot dans l'épreuve
    void tomberDansEpreuve();

    //! Se charge d'effectuer la bonne interruption
    void doInterrupt();
    
    // Péripheriques
    Infrared infrared;
    Lcd lcd;
    Led led;
    LynxMotion lynxMotion;
    Mfs	mfs;
    Motor motor;
    Sonar sonar;
    Sound sound;
    
    // Outils
    QueenTracker queenTracker;
    LineTracker lineTracker;
    
    // Epreuves
    EviterMur eviterMur;
    EviterPoteau eviterPoteau;
    ArcManquant arcManquant;
    VitesseAngulaire vitesseAngulaire;
    CalculerReine calculerReine;
    
    // Le robot a termine?
    bool termine;
private:
    // Etat actuel du robot
    uint8_t mEtat;
    
    // Compteur temporaire pour changer x et y
    uint8_t tmpCounter;
    
    // Timer a time out pour definir les coordonnees au debut
    uint8_t timeOut;
};
</code></pre>

**Options(features)**

**Overview**
