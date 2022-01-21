Projet Space invader

Noms du binôme : Telep Pierre-Louis, Ludwig Julie

Répertoire github : https://github.com/Pierrelouis2/Space_invader

Nous avons créé plusieurs classes : Entity (s’occupe des initialisations (c’est ici que se trouve l’implémentation des listes), de créer le canvas, le joueur et les ennemis), Monde (englobe tout), Joueur (s’occupe du déplacement du joueur, de sa vie et des tirs), Monstres (s’occupe du déplacement des monstres, de leur vies, de leurs nombres et de leurs tirs)

Nous avons ensuite une interface pour executer le programme et tout ce qui concerne la mise en page.

Avec notre Space invaders, nous contrôlons un vaisseau qui tire des missiles, il est possible de se cacher derriere des astéroïdes qui ont une vie limitée et il faut tuer les aliens qui arrivent en haut de la fenêtre et descendent petit à petit. Les aliens tirent des missiles aléatoirement et si le vaisseau est touché le joueur perd une vie. Il y a différent niveaux qui dépendent du nombres d’aliens qui apparaissent. Au dixième niveau il y a un ennemi plus dur à tuer qui apparait (reconnaissable car de couleur orange). En cliquant sur ‘A propos’ les règles du jeu vont apparaître. Le score est comptabilisé au fil de la partie et les vies aussi (il y en a 3 au debut, quand on arrive à zeros la partie est perdue), le bouton ‘Jouer’ lance la partie tandis que le bouton ‘Fermer’ ferme la fenêtre (et arrête le programme).