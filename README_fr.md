Plugins clients pour ExtensiveAutomation
========================================

Plugins pour le client lourd
----------------------

Par défaut, le client lourd est fournie sans plugins.

Les plugins sont à déposer dans le répertoire `Plugins`.
Un redémarrage du client est nécessaire pour le prendre en compte.

Plugins pour les agents
----------------------

Par défaut, la boite à outils est fournie sans plugins.

Les plugins sont à déposer dans le répertoire `Plugins`.
Un redémarrage de la boite à outlis est nécessaire pour le prendre en compte.

Pour supporter l'ensemble des plugins, il est nécessaire d'installer les paquets suivants:

        pip install requests PyMySQL psycopg2 paramiko pymssql ansible kafka