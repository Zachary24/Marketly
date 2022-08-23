from flask import Flask, render_template, request, redirect, url_for
from random import randint
import array
app = Flask(__name__, template_folder='../templates', static_folder='../static')


spots = [
{
'act': 'go',
},

# '1':
{
'act': 'd',
},

# '2':
{
'act': 'chest',
},

# '3':
{
'act': 'd',
},

# '4':
{
'act': 'tax',
},

# '5':
{
'act': 'd',
},

# '6':
{
'act': 'd',
},

# '7':
{
'act': 'd',
},

# '8':
{
'act': 'd',
},

# '9':
{
'act': 'd',
},

# '10':
{
'act': 'd',
},

# '11':
{
'act': 'price-adjustment',
},

# '12':
{
'act': 'd',
},

# '13':
{
'act': 'upgrade-packaging',
},

# '14':
{
'act': 'marketing-campaign',
},

# '15':
{
'act': '',
},

# '16':
{
'act': '',
},

# '17':
{
'act': 'chest',
},

#'18':
{
'act': 'bad-pr',
},

# '19':
{
'act': '',
},

# '20':
{
'act': '',
},

# '21':
{
'act': '',
},

# '22':
{
'act': 'chance',
},

# '23':
{
'act': 'new-billboard',
},

# '24':
{
'act': 'marketing-campaign',
},

# '25':
{
'act': '',
},

# '26':
{
'act': '',
},

# '27':
{
'act': '',
},

# '28':
{
'act': '',
},

# '29':
{
'act': '',
},

# '30':
{
'act': 'jail',
},

# '31':
{
'act': '',
},

# '32':
{
'act': '',
},

# '33':
{
'act': 'chest',
},

# '34':
{
'act': '',
},

# '35':
{
'act': '',
},

# '36':
{
'act': 'chance',
},

# '37':
{
'act': '',
},

# '38':
{
'act': 'luxury-tax',
},

# '39':
{
'act': '',
},

]
#40 total
action=''
roll_num=''
spot = 0
htmlAction = ''
@app.route('/', methods=['GET', 'POST'])
def index():
    global spot
    global action
    global roll_num
    if request.method == 'POST':
        if request.form.get('roll') == 'roll':
            print("roll")
            roll_num = randint(1,10)
            print(roll_num)
            spot = spot + roll_num
            print(spot)
            if spot >= 40:
                print(spot)
                spot = spot - 40
            print(spot)
            action = spots[spot]['act']
            return render_template("index.html", action=action, roll_num=roll_num)
    elif request.method == 'GET':
        return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")
    return action
@app.route('/ran', methods=['GET', 'POST'])
def rand():
    global spot
    global roll_num
    global action
    global htmlAction
    if action == None:
        pass
    if roll_num == None:
        pass
    if spot == None:
        pass
    else:
        htmlAction = """
        You Rolled a %s! <br>
        Your Now at %s <br>
        %s
        """ % (str(roll_num), str(spot), str(action))
    print(htmlAction)
    return str(htmlAction)
