from flask import render_template, flash, redirect, url_for, request
from app import app

# View functions
@app.route('/') # Decorators modify the functions that follow, both / and /index will lead to index page
@app.route('/index')
def index():
    return render_template('index.html', title='Homepage')

@app.route('/about')
def about():
    return render_template('about.html', title='About', 
                                        activePageAbout=True, 
                                        inner_title="About Us", 
                                        description="Who. What. When. Where.", 
                                        landing="aboutLanding" )

@app.route('/why-us')
def why():
    return render_template('why.html', title='Why Us?', 
                                        inner_title="Why Us?", 
                                        description="Insert Text", 
                                        landing="whyLanding")

@app.route('/history')
def history():
    return render_template('history.html', title='History', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")

@app.route('/history/2006')
def history_2006():
    return render_template('history_2006.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")

@app.route('/history/2007')
def history_2007():
    return render_template('history_2007.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")
                                        
@app.route('/history/2008')
def history_2008():
    return render_template('history_2008.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding") 

@app.route('/history/2009')
def history_2009():
    return render_template('history_2009.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")     

@app.route('/history/2010')
def history_2010():
    return render_template('history_2010.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")    

@app.route('/history/2011')
def history_2011():
    return render_template('history_2011.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding") 

@app.route('/history/2012')
def history_2012():
    return render_template('history_2012.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")   

@app.route('/history/2013')
def history_2013():
    return render_template('history_2013.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")    

@app.route('/history/2014')
def history_2014():
    return render_template('history_2014.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")      

@app.route('/history/2015')
def history_2015():
    return render_template('history_2015.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")   

@app.route('/history/2016')
def history_2016():
    return render_template('history_2016.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")   

@app.route('/history/2017')
def history_2017():
    return render_template('history_2017.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")   

@app.route('/history/2018')
def history_2018():
    return render_template('history_2018.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")  

@app.route('/history/2019')
def history_2019():
    return render_template('history_2019.html', title='History 2006', 
                                        inner_title="History", 
                                        description="Insert Text",
                                        landing="historyLanding")                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

@app.route('/leadership')
def leadership():
    return render_template('leadership.html', title='Leadership',
                                        inner_title="Leadership", 
                                        description="Insert Text",
                                        landing="leadershipLanding")

@app.route('/providers')
def providers():
    return render_template('about.html', title='About')

@app.route('/ncqa-and-achc')
def ncqa():
    return render_template('about.html', title='About')