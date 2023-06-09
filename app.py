from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template' )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    
    hulk = ['green', 'heavy', 'weight', 'human', 'strength']
    ironman = ['weapons', 'speed', 'red', 'fly', 'missiles', 'lasers', 'tony', 'helmet', 'jet']
    captain = ['shield', 'leader', 'tactical', 'skils', 'agility', 'stamina', 'blue', 'star', 'stripes']
    black = ['gadgets', 'equipment', 'spy', 'artist', 'espionage', 'black', 'windows symbol', 'tactical boots']
    deadpool = ['swordsman', 'regenerate', 'wade', 'wilson', 'anti', 'hero', 'healing', 'rapid', 'regrow', 'utility belt', 'holsters']
    spiderman = ['wall', 'spider', 'sense', 'red and blue', 'Genius', 'spider symbol', 'web pattren', 'mask']
    vision = ['mind', 'control', 'computer', 'brain', 'self', 'repair', 'vibrant shade of red', 'mind stone', 'android','cape']
    docter = ['time', 'magic', 'illusion', 'dimensional', 'travel', 'vibrant shade of deep red', 'gloves', 'tunic', 'boots']
    falcon = ['pilot', 'flight', 'wing', 'avian telepathy', 'maroon', 'dark red','redwing', 'goggles']
    thanos = ['mad', 'titan', 'telepathy', 'telekinesis', 'infinity gauntlet', 'purple']
    panther = ['panther emblem', 'necklace', 'vibranium']
    thor = ['hammer', 'odinforce', 'wheather', 'silver', 'gold', 'crimson']

    if request.method == 'POST' :
        text = request.form['text'].lower()
        match = any(ask in text for ask in hulk)
        match2 = any(ask in text for ask in ironman)
        match3 = any(ask in text for ask in captain)
        match4 = any(ask in text for ask in black)
        match5 = any(ask in text for ask in deadpool)
        match6 = any(ask in text for ask in spiderman)
        match7 = any(ask in text for ask in vision)
        match8 = any(ask in text for ask in docter)
        match9 = any(ask in text for ask in falcon)
        match10 = any(ask in text for ask in thanos)
        match11 = any(ask in text for ask in panther)
        match12 = any(ask in text for ask in thor)

        if match:
            result = 'hulk' 
        elif match2:
            result = 'ironman' 
        elif match3:
            result = 'captain america'
        elif match4:
            result = 'black window'
        elif match5:
            result = 'deadpool'
        elif match6:
            result = 'spiderman' 
        elif match7:
            result = 'vision'
        elif match8:
            result = 'docter strange'
        elif match9:
            result = 'falcon'
        elif match10:
            result = 'thanos' 
        elif match11:
            result = 'panther'
        elif match12:
            result = 'thor'
        
        else:
            result = 'please type correct avenger characters'                  
       

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)