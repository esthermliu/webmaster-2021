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

@app.route('/behavioral-health-solutions')
def behavioral():
    return render_template('behavioral.html', title='Behavioral Health Solutions',
                                        inner_title="Behavioral Health Solutions",
                                        description="Insert Text",
                                        landing="behavioralLanding")

@app.route('/return-to-work-solutions')
def return_work():
    return render_template('return.html', title='Return-to-Work Solutions',
                                        inner_title="Return-to-Work Solutions",
                                        description="Insert Text",
                                        landing="returnLanding")

@app.route('/virtual-reality-solutions')
def virtual():
    return render_template('virtual.html', title='Virtual Reality Solutions',
                                        inner_title="Virtual Reality Solutions",
                                        description="Insert Text",
                                        landing="virtualLanding") 

@app.route('/mental-disorders-therapy')
def mental():
    return render_template('mental.html', title='Mental Disorders Therapy',
                                        inner_title="Mental Disorders Therapy",
                                        description="Insert Text",
                                        landing="mentalLanding") 

@app.route('/mental-disorders-therapy/<condition>')
def mental_condition(condition):
    conditions_dict = {
        "depression": {
            'template': "depression.html",
            'title': 'Depression'
        }
    }
    if (condition in conditions_dict):
        conditions_specific = conditions_dict[condition]
        return render_template(conditions_specific['template'], title=conditions_specific['title'])
    else:
        return redirect(url_for('mental')) 

@app.route('/physical-therapy')
def physical():
    return render_template('physical.html', title='Physical Therapy',
                                        inner_title="Physical Therapy",
                                        description="Insert Text",
                                        landing="physicalLanding") 

@app.route('/phobia-therapy')
def phobia():
    return render_template('phobia.html', title='Phobia Therapy',
                                        inner_title="Phobia Therapy",
                                        description="Insert Text",
                                        landing="phobiaLanding") 

@app.route('/therapy-dogs')
def dogs():
    return render_template('dog.html', title='Therapy Dogs',
                                        inner_title="Therapy Dogs",
                                        description="Insert Text",
                                        landing="dogLanding") 

@app.route('/therapy-cats')
def cats():
    return render_template('cat.html', title='Therapy Cats',
                                        inner_title="Therapy Cats",
                                        description="Insert Text",
                                        landing="catLanding")   

@app.route('/therapy-horses')
def horses():
    return render_template('horse.html', title='Therapy Horses',
                                        inner_title="Therapy Horses",
                                        description="Insert Text",
                                        landing="horseLanding")   

@app.route('/therapy-rabbits')
def rabbits():
    return render_template('rabbit.html', title='Therapy Rabbits',
                                        inner_title="Therapy Rabbits",
                                        description="Insert Text",
                                        landing="rabbitLanding")  

@app.route('/therapy-reptiles')
def reptiles():
    return render_template('reptile.html', title='Therapy Reptiles',
                                        inner_title="Therapy Reptiles",
                                        description="Insert Text",
                                        landing="reptileLanding")  

@app.route('/therapy-birds')
def birds():
    return render_template('bird.html', title='Therapy Birds',
                                        inner_title="Therapy Birds",
                                        description="Insert Text",
                                        landing="birdLanding")                                       

@app.route('/pet-therapy-solutions')
def pet():
    return render_template('pet.html', title='Pet Therapy Solutions',
                                        inner_title="Pet Therapy Solutions",
                                        description="Insert Text",
                                        landing="petLanding")                                        

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
            'template': "abrasions.html",
            'title': 'Abrasions'
        }
    }
    if (condition in conditions_dict):
        conditions_specific = conditions_dict[condition]
        return render_template(conditions_specific['template'], title=conditions_specific['title'])
    else:
        return redirect(url_for('urgent'))

@app.route('/mens-health')
def mens_health():
    return render_template('men_health.html', title="Men's Health",
                                        inner_title="Men's Health",
                                        description="Insert Text",
                                        landing="menLanding")

@app.route('/mens-health/<condition>')
def mens_health_condition(condition):
    conditions_dict = {
        "dandruff": {
            'template': "dandruff.html",
            'title': 'Dandruff'
        }
    }
    if (condition in conditions_dict):
        conditions_specific = conditions_dict[condition]
        return render_template(conditions_specific['template'], title=conditions_specific['title'])
    else:
        return redirect(url_for('mens_health'))


@app.route('/womens-health')
def womens():
    return render_template('womens_health.html', title="Women's Health",
                                        inner_title="Women's Health",
                                        description="Insert Text",
                                        landing="womenLanding")

@app.route('/womens-health/<condition>')
def womens_health_condition(condition):
    conditions_dict = {
        "dandruff": {
            'template': "dandruff.html",
            'title': 'Dandruff'
        }
    }
    if (condition in conditions_dict):
        conditions_specific = conditions_dict[condition]
        return render_template(conditions_specific['template'], title=conditions_specific['title'])
    else:
        return redirect(url_for('womens'))

@app.route('/teens-health')
def teens_health():
    return render_template('teens_health.html', title="Teen's Health",
                                        inner_title="Teen's Health",
                                        description="Insert Text",
                                        landing="teenLanding")

@app.route('/teens-health/<condition>')
def teens_health_condition(condition):
    conditions_dict = {
        "dandruff": {
            'template': "dandruff.html",
            'title': 'Dandruff'
        }
    }
    if (condition in conditions_dict):
        conditions_specific = conditions_dict[condition]
        return render_template(conditions_specific['template'], title=conditions_specific['title'])
    else:
        return redirect(url_for('teens_health'))

@app.route('/childrens-health')
def childrens_health():
    return render_template('childrens_health.html', title="Children's Health",
                                        inner_title="Children's Health",
                                        description="Insert Text",
                                        landing="childrenLanding")

@app.route('/childrens-health/<condition>')
def childrens_health_condition(condition):
    conditions_dict = {
        "dandruff": {
            'template': "dandruff.html",
            'title': 'Dandruff'
        }
    }
    if (condition in conditions_dict):
        conditions_specific = conditions_dict[condition]
        return render_template(conditions_specific['template'], title=conditions_specific['title'])
    else:
        return redirect(url_for('childrens_health'))

@app.route('/individual-therapy-and-psychiatry')
def therapy():
    return render_template('therapy.html', title="Individual Therapy and Psychiatry",
                                        inner_title="Individual Therapy and Psychiatry",
                                        description="Insert Text",
                                        landing="therapyLanding")

@app.route('/individual-therapy-and-psychiatry/<condition>')
def therapy_condition(condition):
    conditions_dict = {
        "abuse": {
            'template': "abuse.html",
            'title': 'Abuse'
        }
    }
    if (condition in conditions_dict):
        conditions_specific = conditions_dict[condition]
        return render_template(conditions_specific['template'], title=conditions_specific['title'])
    else:
        return redirect(url_for('therapy'))

@app.route('/couples-therapy')
def couples():
    return render_template('couple.html', title="Couples Therapy",
                                        inner_title="Couples Therapy",
                                        description="Insert Text",
                                        landing="coupleLanding")

@app.route('/family-therapy')
def family():
    return render_template('family.html', title="Family Therapy",
                                        inner_title="Family Therapy",
                                        description="Insert Text",
                                        landing="familyLanding")  

@app.route('/speech-therapy')
def speech():
    return render_template('speech.html', title="Speech Therapy",
                                        inner_title="Speech Therapy",
                                        description="Insert Text",
                                        landing="speechLanding")  

@app.route('/occupational-therapy')
def occupational():
    return render_template('occupational.html', title="Occupational Therapy",
                                        inner_title="Occupational Therapy",
                                        description="Insert Text",
                                        landing="occupationalLanding")        

@app.route('/covid-19-testing')
def covid_19():
    return render_template('covid.html', title="COVID-19 Testing",
                                        inner_title="COVID-19 Testing",
                                        description="Insert Text",
                                        landing="covidLanding")  

@app.route('/covid-19-screening-and-treatment')
def screening():
    return render_template('screening.html', title="COVID-19 Screening and Treatment",
                                        inner_title="COVID-19 Screening and Treatment",
                                        description="Insert Text",
                                        landing="screeningLanding")  

@app.route('/how-it-works')
def how():
    return render_template('how.html', title="How It Works",
                                        inner_title="How It Works",
                                        description="Insert Text",
                                        landing="howLanding") 

@app.route('/pricing-and-insurance')
def pricing():
    return render_template('pricing.html', title="Pricing and Insurance",
                                        inner_title="Pricing and Insurance",
                                        description="Insert Text",
                                        landing="priceLanding") 

@app.route('/our-app')
def app():
    return render_template('app.html', title="Our App",
                                        inner_title="Our App",
                                        description="Insert Text",
                                        landing="appLanding") 
                           