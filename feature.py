from flask import Flask

FAI=Flask(__name__)

@FAI.route('/StringResponse')
def StringResponse():
    return '<center><h1 style="background-color:blue">This is the First View of Flask Project</h1></center>'


@FAI.route('/SecondStringResponse')
def SecondStringResponse():
    return '<center><h1 style="background-color:red">This is the Second View of Flask Project</h1></center>'

if __name__=='__main__':
    FAI.run(debug=True)

