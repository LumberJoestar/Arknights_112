#The Operators Class, or the Tower Class
class Operator:
    def __init__(self,name,group,profession,subprofession,maxHP,atk,defence,artResis,atkTime,atkRange,cost,block):
        self.name=name
        self.group=group
        self.profession=profession
        self.subprofession=subprofession
        self.maxHP=maxHP
        self.atk=atk
        self.defence=defence
        self.artResis=artResis
        self.atkTime=atkTime
        self.atkRange=atkRange
        self.cost=cost
        self.block=block
        self.currentBlock=0
        self.atkSpeed=100
        self.taunt=0
        self.currentHP=maxHP
        self.buff=[]
        self.debuff=[]

#The profession class:
class Profession():
    def __init__(self,description):
        self.description=description

#8 professions are the subclasses of Profession()
class Vanguard(Profession):
    def __init__(self,description):
        super.__init__(description)

class Guard(Profession):
    def __init__(self,description):
        super.__init__(description)

class Sniper(Profession):
    def __init__(self,description):
        super.__init__(description)

class Caster(Profession):
    def __init__(self,description):
        super.__init__(description)

class Defender(Profession):
    def __init__(self,description):
        super.__init__(description)

class Medic(Profession):
    def __init__(self,description):
        super.__init__(description)

class Specialist(Profession):
    def __init__(self,description):
        super.__init__(description)

class Supporter(Profession):
    def __init__(self,description):
        super.__init__(description)

#Sub professions:
class Pioneer(Vanguard):
    def __init__(self,description):
        super.__init__(description)
        self.description='Blocks 2 enemies'

class Charger(Vanguard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Obtain 1 DP after this unit defeats an enemy;
                         Refunds the original DP Cost when retreated.
                        '''

class StandardBearer(Vanguard):
    def __init__(self,description):
        super.__init__(description)
        self.description='Cannot block enemies during the skill duration.'

class Tactician(Vanguard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         This unit can designate one Tactical Point within attack range to call Reinforcements; 
                         ATK is increased to 150% when attacking enemies blocked by Reinforcements.
                         '''
class Agent(Vanguard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Has reduced Redeployment Time; 
                         Can attack enemies from range.	
                         '''
class Dreadnought(Guard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Blocks 1 enemy	
                         '''

class Centurion(Guard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Attacks multiple enemies equal to Block count.	
                         '''

class Lord(Guard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Can launch Ranged Attacks that deal 80'%' of normal ATK.	
                         '''

class ArtsFighter(Guard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Deals Arts Damage	
                         '''

class Instructor(Guard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Can attack enemies from range; 
                         When attacking enemies not blocked by self, increase ATK to 120%.	
                         '''

class Fighter(Guard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Blocks 1 enemy	
                         '''

class Swordmaster(Guard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Normal attacks deal damage twice.	
                         '''

class Musha(Guard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Can't be healed by other units. 
                         Recovers 70 self HP every time this operator attacks an enemy.	
                         '''

class Liberator(Guard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         	Normally does not attack and has 0 Block; 
                            When skill is inactive, ATK gradually increases up to +200% over 40 seconds. 
                            ATK is reset when the skill ends.	
                         '''

class Reaper(Guard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Cannot be healed by allies; Attacks deal AoE damage; 
                         Recovers 50 HP for every enemy hit during attacks, up to Block count.	
                         '''

class Crusher(Guard):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Attacks multiple enemies equal to Block count.
                         '''

class Marksman(Sniper):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Attacks aerial enemies first.	
                         '''
    
class Marksman(Sniper):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Deals AOE Physical Damage.	
                         '''

class Deadeye(Sniper):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Prioritizes attacking the enemy with lowest DEF within range first.	
                         '''

class Heavyshooter(Sniper):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         High-accuracy point-blank shot.	
                         '''

class Spreadshooter(Sniper):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         	Attacks all enemies within range, and deals 150% damage to enemies in the row directly in front of this unit.	
                         '''

class Besieger(Sniper):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Attacks the heaviest enemy first.		
                         '''

class Flinger(Sniper):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         	Attacks deal two instances of Physical damage to ground enemies in a small area 
                            (The second instance is a shockwave that has half the normal ATK).		
                         '''

class Core(Caster):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Deals Arts Damage.			
                         '''

class Splash(Caster):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Deals AOE Arts Damage.			
                         '''

class Blast(Caster):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Deals AOE Arts Damage in a long line.				
                         '''

class Blast(Caster):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         	Attacks deal Arts damage and jump to 4 other enemies. 
                            Each jump deals 15% less damage and inflicts a brief Slow.			
                         '''

class MechAccord(Caster):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         	Controls a Drone to deal Arts damage to an enemy; 
                            When the Drone continuously attacks the same enemy, its damage will increase (up to 110% of the operator's ATK).				
                         '''

class Phalanx(Caster):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Normally does not attack, but has greatly increased DEF and RES; 
                         When skill is active, attacks deal AoE Arts Damage.				
                         '''

class Mystic(Caster):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Attacks deal Arts damage; 
                         When unable to find a target, attacks can be stored up and fired all at once (Up to 3 charges).				
                         '''

class Protector(Defender):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Blocks 3 enemies				
                         '''

class Guardian(Defender):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Can heal allies by using the skill.					
                         '''

class Juggernaut(Defender):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Cannot be healed by allies.						
                         '''

class ArtsProtector(Defender):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Normal attacks deal Arts damage while the skill is active.							
                         '''

class Duelist(Defender):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Only restores SP when blocking enemies.								
                         '''

class Fortress(Defender):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         When not blocking enemies, prioritizes dealing ranged AoE Physical damage.									
                         '''

class Fortress(Defender):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Blocks 3 enemies; Can launch Ranged Attacks.	
                         '''

class Med(Medic):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Restores the HP of allies.						
                         '''

class MultiTarget(Medic):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Restores the HP of 3 allies simultaneously.						
                         '''

class Therapist(Medic):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Has a large healing range, but the healing amount on farther targets is reduced to 80%.					
                         '''

class Wandering(Medic):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Restores the HP of allied units and recovers Elemental Damage by 50% of ATK (can recover Elemental Damage of unhurt allied units).						
                         '''

class Incanation(Medic):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Attacks deal Arts damage; 
                         When attacking an enemy, heals an allied Operator within range equal to 50% of the damage dealt.					
                         '''

class Chain(Medic):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         	Restores the HP of allies and jumps between 3 other allies. 
                            Each jump restores 25% less HP.	
                         '''

class PushStroker(Specialist):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Can attack multiple enemies equal to Block count.
                         Can be deployed on Ranged Tiles.
                         '''

class Hookmaster(Specialist):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         	Can Shift enemies by using skills.
                            Can be deployed on Ranged Tiles.
                         '''

class Executor(Specialist):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         	Significantly reduced Redeployment Time.
                         '''

class Ambusher(Specialist):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Deals Damage to all targets within range.
                         50% chance to dodge Physical and Arts attacks and is less likely to be targeted by enemies.							
                         '''

class Geek(Specialist):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         	Continually loses HP over time.	
                         '''

class Merchant(Specialist):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                 		Has reduced Redeployment Time, but DP Cost is not refunded upon retreating; 
                        While deployed, 3 DP are consumed every 3 seconds 
                        (automatically retreats without sufficient DP).
                         '''

class Trapmaster(Specialist):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         	Can use traps to assist in combat, but traps cannot be placed on tiles already occupied by an enemy.
                         '''   

class Geek(Specialist):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                        Does not retreat upon receiving lethal damage, instead swaps to a <Substitute> (Substitute has 0 Block). 
                        Swaps back to the original after 20 seconds.	
                         '''

class DecelBinder(Supporter):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Deals Arts Damage and Slows the target for a short time.		
                         '''

class Summoner(Supporter):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                        Deals Arts Damage.
                        Can use Summons in battles.			
                         '''

class DecelBinder(Supporter):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                        Deals Arts Damage.
                        Can use Summons in battles.			
                         '''

class Hexer(Supporter):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Deals Arts Damage.			
                         '''

class Bard(Supporter):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Does not attack but continuously restores the HP of all allies within range (the HP restored per second is equal to 10% of self ATK). 
                         Self is unaffected by Inspiration.		
                         '''

class Abjurer(Supporter):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                        Deals Arts Damage; 
                        When the skill is active, attacks instead restore the HP of allies (heal amount is equal to 75% of ATK).			
                         '''

class Artificer(Supporter):
    def __init__(self,description):
        super.__init__(description)
        self.description='''
                         Blocks 2 enemies; 
                         Can use <Support Devices> in battles.				
                         '''



