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
                                        description="Who. What. When. Where. Why.", 
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

@app.route('/history/<int:year>')
def history_year(year):
    whitelist_years = {
        2006: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        },
        2007: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        },
        2008: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }, 
        2009: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }, 
        2010: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }, 
        2011: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }, 
        2012: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }, 
        2013: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }, 
        2014: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }, 
        2015: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }, 
        2016: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }, 
        2017: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }, 
        2018: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }, 
        2019: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'historyLanding',
            'description': 'Insert Text'
        }
    }

    if (year in whitelist_years):
        specific_year = whitelist_years[year]
        return render_template(specific_year['template'], title=specific_year['title'],
                                                        inner_title=specific_year['inner_title'],
                                                        landing=specific_year['landing'],
                                                        description=specific_year['description'],
                                                        year=year)
    else:
        return redirect('/history')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

@app.route('/leadership')
def leadership():
    return render_template('leadership.html', title='Leadership',
                                        inner_title="Leadership", 
                                        description="Insert Text",
                                        landing="leadershipLanding")

@app.route('/leadership/<leader>')
def leadership_bio(leader):
    leaders_dict = {
        "Sammy": {
            'template': 'sammy.html',
            'title': 'Sammy Urtzal', 
            'inner_title': 'Sammy Urtzal', 
            'description': 'Insert Text',
            'landing': 'sammyLanding'         
        }
    }

    if (leader in leaders_dict):
        specific_leader = leaders_dict[leader]
        return render_template(specific_leader['template'], title=specific_leader['title'],
                                            inner_title=specific_leader['inner_title'], 
                                            description=specific_leader['description'],
                                            landing=specific_leader['landing'])
    else:
        return redirect(url_for('leadership'))

@app.route('/providers')
def providers():
    return render_template('providers.html', title='Our Providers',
                                        inner_title="Our Providers",
                                        description="Insert Text",
                                        landing="providersLanding")

@app.route('/ncqa-and-achc')
def ncqa():
    return render_template('ncqa.html', title='NCQA and ACHC',
                                        inner_title="NCQA and ACHC",
                                        description="Insert Text",
                                        landing="ncqaLanding")

@app.route('/treatment-options')
def treatment():
    return render_template('treatment.html', title='Treatment Options',
                                        inner_title="Treatment Options",
                                        description="Insert Text",
                                        landing="treatmentLanding")

@app.route('/medical-health-solutions')
def medical():
    return render_template('medical.html', title='Medical Health Solutions',
                                        inner_title="Medical Health Solutions",
                                        description="Insert Text",
                                        landing="medicalLanding")

@app.route('/urgent-care')
def urgent():
    return render_template('urgent.html', title='Urgent Care',
                                        inner_title="Urgent Care",
                                        description="Insert Text",
                                        landing="urgentLanding")

@app.route('/urgent-care/<condition>')
def urgent_condition(condition):
    conditions_dict = {
        "abrasions": {
            'template': "abrasions.html"
        }
    }
    if (condition in conditions_dict):
        conditions_specific = conditions_dict[condition]
        return render_template(conditions_specific['template'], title='Urgent Care',
                                        inner_title="Urgent Care",
                                        description="Insert Text",
                                        landing="urgentLanding")
    else:
        return redirect(url_for('urgent'))