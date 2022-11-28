from cmu_112_graphics import *
#The Operators Class, or the Tower Class
class Operator:
    def __init__(self,name,group,maxHP,atk,defence,cost):
        #Properties that needs to be initialized
        self.name=name
        self.group=group
        self.maxHP=maxHP
        self.atk=atk
        self.defence=defence
        self.cost=cost
         
        #Some common properties
        self.currentBlock=0
        self.atkSpeed=100
        self.taunt=0
        self.currentHP=maxHP
        self.buff=[]
        self.debuff=[]
        
        #These properties are the same for the subprofessions
        #self.block=block
        #self.artResis=artResis
        #self.atkTime=atkTime
        #self.atkRange=atkRange
        #self.redeployTime=redeployTime
        

#8 professions are the subclasses of Operators()
class Vanguard(Operator):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)

class Guard(Operator):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)

class Sniper(Operator):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)

class Caster(Operator):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)

class Defender(Operator):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)

class Medic(Operator):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)

class Specialist(Operator):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)

class Supporter(Operator):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)

#Sub professions:
#The ones that are not kept for MVP is commented out
class Pioneer(Vanguard):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='Blocks 2 enemies'
        self.block=2
        self.artResis=0
        self.atkTime=1.05
        self.atkRange=[['Center',True]]
        self.redeployTime=70

class Charger(Vanguard):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Obtain 1 DP after this unit defeats an enemy;
                         Refunds the original DP Cost when retreated.
                        '''
        self.block=1
        self.artResis=0
        self.atkTime=1.0
        self.atkRange=[['Center',True]]
        self.redeployTime=70

#class StandardBearer(Vanguard):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='Cannot block enemies during the skill duration.'

#class Tactician(Vanguard):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #This unit can designate one Tactical Point within attack range to call Reinforcements; 
                         #ATK is increased to 150% when attacking enemies blocked by Reinforcements.
                         #'''
#class Agent(Vanguard):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Has reduced Redeployment Time; 
                         #Can attack enemies from range.	
                         #'''
class Dreadnought(Guard):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Blocks 1 enemy	
                         '''
        self.block=1
        self.artResis=0
        self.atkTime=1.5
        self.atkRange=[['Center',True]]
        self.redeployTime=70

class Centurion(Guard):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Attacks multiple enemies equal to Block count.	
                         '''
        self.block=3
        self.artResis=0
        self.atkTime=1.2
        self.atkRange=[['Center',True]]
        self.redeployTime=70

class Lord(Guard):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Can launch Ranged Attacks that deal 80'%' of normal ATK.	
                         '''
        self.block=2
        self.artResis=10
        self.atkTime=1.3
        self.atkRange=[[True,True,False,False],
                       ['Center',True,True,True],
                       [True,True,False,False]]
        self.redeployTime=70

#class ArtsFighter(Guard):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Deals Arts Damage	
                         #'''

#class Instructor(Guard):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Can attack enemies from range; 
                         #When attacking enemies not blocked by self, increase ATK to 120%.	
                         #'''

#class Fighter(Guard):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Blocks 1 enemy	
                         #'''

#class Swordmaster(Guard):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Normal attacks deal damage twice.	
                         #'''

#class Musha(Guard):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Can't be healed by other units. 
                         #Recovers 70 self HP every time this operator attacks an enemy.	
                         #'''

#class Liberator(Guard):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         	#Normally does not attack and has 0 Block; 
                            #When skill is inactive, ATK gradually increases up to +200% over 40 seconds. 
                            #ATK is reset when the skill ends.	
                         #'''

#class Reaper(Guard):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Cannot be healed by allies; Attacks deal AoE damage; 
                         #Recovers 50 HP for every enemy hit during attacks, up to Block count.	
                         #'''

#class Crusher(Guard):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Attacks multiple enemies equal to Block count.
                         #'''

class Marksman(Sniper):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Attacks aerial enemies first.	
                         '''
        self.block=1
        self.artResis=0
        self.atkTime=1.0
        self.atkRange=[[True,True,True,True],
                       ['Center',True,True,True],
                       [True,True,True,True]]
        self.redeployTime=70
    
class Artilleryman(Sniper):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Deals AOE Physical Damage.	
                         '''
        self.block=1
        self.artResis=0
        self.atkTime=2.8
        self.atkRange=[[True,True,True,True,True],
                       ['Center',True,True,True,True],
                       [True,True,True,True,True]]
        self.redeployTime=70

class Deadeye(Sniper):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Prioritizes attacking the enemy with lowest DEF within range first.	
                         '''
        self.block=1
        self.artResis=0
        self.atkTime=2.7
        self.atkRange=[[True,True,True,False,False]
                       [True,True,True,True,False],
                       ['Center',True,True,True,True],
                       [True,True,True,True,False],
                       [True,True,True,False,False]]
        self.redeployTime=70
#class Heavyshooter(Sniper):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #High-accuracy point-blank shot.	
                         #'''

#class Spreadshooter(Sniper):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         	#Attacks all enemies within range, and deals 150% damage to enemies in the row directly in front of this unit.	
                         #'''

#class Besieger(Sniper):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Attacks the heaviest enemy first.		
                         #'''

#class Flinger(Sniper):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         	#Attacks deal two instances of Physical damage to ground enemies in a small area 
                            #(The second instance is a shockwave that has half the normal ATK).		
                         #'''

class Core(Caster):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Deals Arts Damage.			
                         '''
        self.block=1
        self.artResis=20
        self.atkTime=1.6
        self.atkRange=[[True,True,True,False],
                       ['Center',True,True,True],
                       [True,True,True,False]]
        self.redeployTime=70

class Splash(Caster):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Deals AOE Arts Damage.			
                         '''
        self.block=1
        self.artResis=20
        self.atkTime=2.9
        self.atkRange=[[True,True,True],
                       ['Center',True,True],
                       [True,True,True]]
        self.redeployTime=70

#class Blast(Caster):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                        #Deals AOE Arts Damage in a long line.				
                         #'''

#class Chain(Caster):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         	#Attacks deal Arts damage and jump to 4 other enemies. 
                            #Each jump deals 15% less damage and inflicts a brief Slow.			
                         #'''

#class MechAccord(Caster):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         	#Controls a Drone to deal Arts damage to an enemy; 
                            #When the Drone continuously attacks the same enemy, its damage will increase (up to 110% of the operator's ATK).				
                         #'''

#class Phalanx(Caster):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Normally does not attack, but has greatly increased DEF and RES; 
                         #When skill is active, attacks deal AoE Arts Damage.				
                         #'''

#class Mystic(Caster):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Attacks deal Arts damage; 
                         #When unable to find a target, attacks can be stored up and fired all at once (Up to 3 charges).				
                         #'''

class Protector(Defender):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Blocks 3 enemies				
                         '''
        self.block=3
        self.artResis=0
        self.atkTime=1.2
        self.atkRange=[['Center',True]]
        self.redeployTime=70

class Guardian(Defender):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Can heal allies by using the skill.					
                         '''
        self.block=3
        self.artResis=10
        self.atkTime=1.2
        self.atkRange=[['Center']]
        self.redeployTime=70

#class Juggernaut(Defender):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Cannot be healed by allies.						
                         #'''

#class ArtsProtector(Defender):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Normal attacks deal Arts damage while the skill is active.							
                         #'''

#class Duelist(Defender):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Only restores SP when blocking enemies.								
                         #'''

#class Fortress(Defender):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #When not blocking enemies, prioritizes dealing ranged AoE Physical damage.									
                         #'''

#class Sentinel(Defender):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Blocks 3 enemies; Can launch Ranged Attacks.	
                         #'''

class Med(Medic):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Restores the HP of allies.						
                         '''
        self.block=1
        self.artResis=0
        self.atkTime=2.85
        self.atkRange=[[True,True,True,True],
                       ['Center',True,True,True],
                       [True,True,True,True]]
        self.redeployTime=70

class MultiTarget(Medic):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Restores the HP of 3 allies simultaneously.						
                         '''
        self.block=1
        self.artResis=5
        self.atkTime=2.85
        self.atkRange=[[True,True,True,True],
                       [True,'Center',True,True],
                       [True,True,True,True]]
        self.redeployTime=70

#class Therapist(Medic):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Has a large healing range, but the healing amount on farther targets is reduced to 80%.					
                         #'''

#class Wandering(Medic):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Restores the HP of allied units and recovers Elemental Damage by 50% of ATK (can recover Elemental Damage of unhurt allied units).						
                         #'''

#class Incanation(Medic):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Attacks deal Arts damage; 
                         #When attacking an enemy, heals an allied Operator within range equal to 50% of the damage dealt.					
                         #'''

#class Chain(Medic):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         	#Restores the HP of allies and jumps between 3 other allies. 
                            #Each jump restores 25% less HP.	
                         #'''

class PushStroker(Specialist):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Can attack multiple enemies equal to Block count.
                         Can be deployed on Ranged Tiles.
                         '''
        self.block=2
        self.artResis=0
        self.atkTime=1.2
        self.atkRange=[['Center',True]]
        self.redeployTime=70

class Hookmaster(Specialist):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         	Can Shift enemies by using skills.
                            Can be deployed on Ranged Tiles.
                         '''
        self.block=2
        self.artResis=0
        self.atkTime=1.8
        self.atkRange=[['Center',True,True,True]]
        self.redeployTime=70

class Executor(Specialist):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         	Significantly reduced Redeployment Time.
                         '''
        self.block=1
        self.artResis=0
        self.atkTime=0.93
        self.atkRange=[['Center',True]]
        self.redeployTime=18

class Ambusher(Specialist):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Deals Damage to all targets within range.
                         50% chance to dodge Physical and Arts attacks and is less likely to be targeted by enemies.							
                         '''
        self.block=0
        self.artResis=30
        self.atkTime=3.5
        self.atkRange=[[True,True,True,False],
                       [True,'Center',True,True],
                       [True,True,True,False]]
        self.redeployTime=70


#class Geek(Specialist):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         	#Continually loses HP over time.	
                         #'''

#class Merchant(Specialist):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                 		#Has reduced Redeployment Time, but DP Cost is not refunded upon retreating; 
                        #While deployed, 3 DP are consumed every 3 seconds 
                        #(automatically retreats without sufficient DP).
                         #'''

#class Trapmaster(Specialist):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         	#Can use traps to assist in combat, but traps cannot be placed on tiles already occupied by an enemy.
                         #'''   

#class DollKeeper(Specialist):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                        #Does not retreat upon receiving lethal damage, instead swaps to a <Substitute> (Substitute has 0 Block). 
                        #Swaps back to the original after 20 seconds.	
                         #'''

class DecelBinder(Supporter):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                         Deals Arts Damage and Slows the target for a short time.		
                         '''
        self.block=1
        self.artResis=25
        self.atkTime=1.9
        self.atkRange=[[True,True,True,True],
                       [True,'Center',True,True],
                       [True,True,True,True]]
class Summoner(Supporter):
    def __init__(self,name,group,maxHP,atk,defence,cost):
        super().__init__(name,group,maxHP,atk,defence,cost)
        self.description='''
                        Deals Arts Damage.
                        Can use Summons in battles.			
                         '''
        self.block=1
        self.artResis=20
        self.atkTime=1.6
        self.atkRange=[[True,True,True,False],
                       ['Center',True,True,True],
                       [True,True,True,False]]

#class Hexer(Supporter):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Deals Arts Damage.			
                         #'''

#class Bard(Supporter):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Does not attack but continuously restores the HP of all allies within range (the HP restored per second is equal to 10% of self ATK). 
                         #Self is unaffected by Inspiration.		
                         #'''

#class Abjurer(Supporter):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                        #Deals Arts Damage; 
                        #When the skill is active, attacks instead restore the HP of allies (heal amount is equal to 75% of ATK).			
                         #'''

#class Artificer(Supporter):
    #def __init__(self,name,group,maxHP,atk,defence,cost):
        #super.__init__(name,group,maxHP,atk,defence,cost)
        #self.description='''
                         #Blocks 2 enemies; 
                         #Can use <Support Devices> in battles.				
                         #'''



