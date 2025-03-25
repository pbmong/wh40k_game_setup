
main_missions_list =[
    {
        "name":"Take and hold",
        "description":
            "TAKE AND HOLD\n\n\
- Special: NA \n\n\
- Battle Round 2-4: At the end of each Command phase, the player whose turn it is scores 5VP for each objective\n\
  marker they control (up to 15VP per turn). \n\
- Battle Round 5: The player who has the first turn scores VP as described above. The player who has the second\n\
  turn scores VP as described above, but does so at the end of their turn instead of at the end of their Command phase.\n\n\
- End of Battle: NA\
    "
    },
    {
        "name":"",
        "description":
            "SCHORCHED EARTH\n\n\
- Special: From the second battle round, in each player’s Shooting phase, the player whose turn it is can select\n\
  one unit from their army that is not Battle-shocked and is eligible to shoot. Until the end of that turn, that\n\
  unit is not eligible to shoot or declare a charge. At the start of its controlling player’s next Command phase,\n\
  if that unit is within 1” of an objective marker that the player whose turn it is controls, that objective marker\n\
  is burned and removed from the battlefield \n\n\
- Battle Round 2-4: At the end of each Command phase, the player whose turn it is scores 5VP for each objective\n\
  marker they control (up to 15VP per turn).\n\n\
- Battle Round 5: The player who has the first turn scores VP as described above. The player who has the second\n\
  turn scores VP as described above, but does so at the end of their turn instead of at the end of their Command phase.\n\n\
- End of Battle: Each player scores 5VP if one or more objective markers in No Man’s Land were burned by a unit\n\
  from their army, and 10VP if the objective marker in their opponent’s deployment zone was burned.\
    "
    },
    {
        "name":"",
        "description":
            "PURGE THE FOE\n\n\
- Special: At the end of the battle round, each player scores 4VP if one of more enemy units were destroyed that\n\
  battle round, and an extra 4VP if more enemy units than friendly units were destroyed that battle round. \n\
  Note that a unit can, if it is returned to the battlefield for any reason, potentially contribute to this\n\
  Primary Mission several times (assuming it is returned and subsequently destroyed several times over) \n\n\
- Battle Round 2-4: At the end of each Command phase, the player whose turn it is scores 4VP if they control one\n\
  or more objective markers, and an extra 4VP if they control more objective markers than their opponent controls.\n\n\
- Battle Round 5: The player who has the first turn scores VP as described above. The player who has the second\n\
  turn scores VP as described above, but does so at the end of their turn instead of at the end of their Command phase.\n\n\
- End of Battle: NA\
            "
    },
    {
        "name":"",
        "description":
            "SITES OF POWER\n\n\
- Special: The objective markers in No Man’s Land are sites of power. At the end of each command phase, the player\n\
 whose turn it is empowers all sites of power that they control that have one or more Character models from their\n\
 army within range; each site of power remains empowered by that player while one or more of their Character models\n\
 remains within range of it \n\n\
- Battle Round 2-4: At the end of each player’s Command phase, the player whose turn it is scores VP as follows\n\
(up to 15VP per turn):\n\
    ● 3VP for each objective marker they control\n\
    ● 3VP for each site of power they have empowered\n\
Note that these are cumulative, so a player that controls one objective marker they have also empowered will score 6VP\n\
that turn\n\n\
- Battle Round 5: The player who has the first turn scores VP as described above. The player who has the second\n\
  turn scores VP as described above, but does so at the end of their turn instead of at the end of their Command phase.\n\n\
- End of Battle: NA\
            "
    },
    {
        "name":"",
        "description":
            "PRIORITY TARGETS\n\n\
- Special: NA \n\n\
- Battle Round 2-5: At the end of each Command phase, the player whose turn it is scores 5VP for each objective\n\
  marker they control (up to 10VP per turn).\n\n\
- End of Battle: Each player scores 5VP for each objective marker they control (up to 15VP per player)\
            "
    },
    {
        "name":"",
        "description":
            "SUPPLY DROP\n\n\
- Special: At the start of the battle, players randomly select two different objective markers in No Man’s Land:\n\
  the first selected is the Alpha objective, the second is the Omega objective. At the start of the fourth battle\n\
  round, the Alpha objective is removed from the battlefield. At the start of the fifth battle round, all objective\n\
  markers in No Man’s Land apart from the Omega objective are also removed. \n\n\
- Battle Round 2-3: At the end of each Command phase, the player whose turn it is scores 5VP for each objective\n\
  marker they control in No Man’s Land.\n\n\
- Battle Round 4: At the end of each Command phase, the player whose turn it is scores 8VP for each objective\n\
  marker they control in No Man’s Land.\n\n\
- Battle Round 5: The player who has the first turn scores 15VP at the end of their command phase if they control\n\
  the objective marker in No Man’s Land. The player who has the second turn scores 15VP at the end of their turn\n\
  if they control the objective maker in No Man’s Land.\n\n\
- End of Battle: NA\
            "
    },
    {
        "name":"",
        "description":
            "VITAL GROUND\n\n\
- Special: If you draw this and the Hidden Supplies Mission Rule Card, discard this card and draw a new Primary\n\
  Mission card. After setting up the battlefield, remove the objective marker in No Man’s Land that is closest\n\
  to the centre of the battlefield. \n\n\
- Battle Round 2-4: At the end of each Command phase, the player whose turn it is scores VP as follows:\n\
    ● If they control the objective marker in their own deployment zone, they score 2VP.\n\
    ● For each objective marker in No Man’s Land they control, they score 5VP.\n\
    ● If they control the objective marker in their opponent’s deployment zone, they score 6VP.\n\n\
- Battle Round 5: The player who has the first turn scores VP as described above. The player who has the second turn\n\
  scores VP as described above, but does so at the end of their turn instead of at the end of their Command phase.\n\n\
- End of Battle: NA\
            "
    }
]

missions_rules_list =[
    {
        "name":"CHILLING RAIN",
        "description":
            "CHILLING RAIN\n\n\
In this mission, no additional mission rules apply                                                                \n\
"
    },
    {
        "name":"HIDDEN SUPPPLIES",
        "description":
            "HIDDEN SUPPPLIES\n\n\
In this mission, players must set up one additional objective marker in No Man’s Land. Unless the Chosen Battlefield\n\
mission rule is also in effect, before setting up this new objective marker, players must first move the objective\n\
marker in the centre of the battlefield 6” directly towards one of the corners of the battlefield (if No Man’s Land\n\
touches any corners of the battlefield, you must move the objective marker towards one of those corners). Players\n\
then set up the new objective marker 6” from the centre of the battlefield towards the diagonally opposite corner\n\
of the battlefield to the previously moved objective marker.\
"
    },
    {
        "name":"MINEFIELDS",
        "description":
            "MINEFIELDS\n\n\
In this mission, each time an Advance roll of 6 is made for a unit, that unit suffers 1 mortal wound.\
"
    },
    {
        "name":"SCRAMBLER FIELDS",
        "description":
            "SCRAMBLER FIELDS\n\
In this mission unit cannot be set up within range of an objective marker that is either in No Man’s\n\
Land or their opponent’s deployment zone for:\n\
● Players’ units with the Infiltrators ability. \n\
● Players’ units with the Scout ability that make a move before the first turn begins. \n\
● If any rule is used to redeploy a unit.\n\
● Setting up Reserves and Strategic Reserves units on battelfield, including opponent’s deployment zone.\n\
"
    },
    {
        "name":"DELAYED RESERVES",
        "description":
            "DELAYED RESERVES\n\n\
In this mission, until the start of the third battle round, each time a Reserves or Strategic Reserves unit wishes\n\
to arrive on the battlefield, the controlling player must make a Reserves roll for it. To do so, that player rolls\n\
one D6: on a 3+, that unit arrives on the battlefield; otherwise, the Reserves roll fails and that unit does not\n\
arrive this turn.\
"
    },
    {
        "name":"SUPPLY LINES",
        "description":
            "SUPPLY LINES\n\n\
In this mission, if a player controls the objective marker in their own deployment zone at the start of their\n\
Command phase, they roll one D6: on a 4+, that player gains 1CP.\
"
    },
    {
        "name":"VOX STATIC",
        "description":
            "VOX STATIC\n\n\
In this mission, the Command Re-roll Stratagem and New Orders Stratagem both cost 2CP to use.\
"
    }]