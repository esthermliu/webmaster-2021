from flask import render_template, flash, redirect, url_for, request
from app import app, posts, news_articles, blog_articles, login
from app import db
from app.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm, MakeAppointmentForm, UserAccount, AllergyForm, SurgeryForm, ConditionForm
from app.models import User, Appointments, Allergies, Surgeries, Conditions
from flask_login import logout_user, login_required
from flask_login import current_user, login_user
from werkzeug.urls import url_parse
import math
from flaskext.markdown import Markdown
from app.email import send_password_reset_email, send_appointment_email
from datetime import datetime, timedelta, timezone

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
                                        description="Our story thus far",
                                        landing="historyLanding")

@app.route('/history/<int:year>')
def history_year(year):
    whitelist_years = {
        1996: {
            'template': 'history_1996.html',
            'title': 'History 1996',
            'inner_title': 'History',
            'landing': 'humbleLanding',
            'description': '1996'
        },
        2006: {
            'template': 'history_2006.html',
            'title': 'History 2006',
            'inner_title': 'History',
            'landing': 'teamLanding',
            'description': '2006 - 2009'
        },
        2009: {
            'template': 'history_2009.html',
            'title': 'History 2009',
            'inner_title': 'History',
            'landing': 'landing2009',
            'description': '2009 - 2012'
        },  
        2012: {
            'template': 'history_2012.html',
            'title': 'History 2012',
            'inner_title': 'History',
            'landing': 'landing2012',
            'description': '2012-2016'
        }, 
        2016: {
            'template': 'history_2016.html',
            'title': 'History 2016',
            'inner_title': 'History',
            'landing': 'landing2016',
            'description': '2016-2021'
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
                                        description="The People Behind the Magic",
                                        landing="leadershipLanding")

@app.route('/leadership/<leader>')
def leadership_bio(leader):
    leaders_dict = {
        "Sammy": {
            'template': 'sammy.html',
            'title': 'Sammy Urtzal', 
            'inner_title': 'Sammy Urtzal', 
            'description': 'Founder & CEO',
            'landing': 'sammyLanding'         
        },
        "Josephine": {
            'template': 'josephine.html',
            'title': 'Josephine Greenberg', 
            'inner_title': 'Josephine Greenberg', 
            'description': 'COO',
            'landing': 'joLanding'         
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
                                        description="Our Solutions",
                                        landing="treatmentLanding")

@app.route('/medical-health-solutions')
def medical():
    return render_template('medical.html', title='Medical Health Solutions',
                                        inner_title="Medical Health Solutions",
                                        description="Physical Care, Done Virtually",
                                        landing="medicalLanding")

@app.route('/behavioral-health-solutions')
def behavioral():
    return render_template('behavioral.html', title='Behavioral Health Solutions',
                                        inner_title="Behavioral Health Solutions",
                                        description="Prioritizing Mental Health",
                                        landing="behavioralLanding")

@app.route('/return-to-work-solutions')
def return_work():
    return render_template('return.html', title='Return-to-Work Solutions',
                                        inner_title="Return-to-Work Solutions",
                                        description="Addressing the pandemic, together",
                                        landing="returnLanding")

@app.route('/virtual-reality-solutions')
def virtual():
    return render_template('virtual.html', title='Virtual Reality Solutions',
                                        inner_title="Virtual Reality Solutions",
                                        description="Pioneers of Medical VR",
                                        landing="virtualLanding") 

@app.route('/mental-disorders-therapy')
def mental():
    return render_template('mental.html', title='Mental Disorders Therapy',
                                        inner_title="Mental Disorders Therapy",
                                        description="Get started now",
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
                                        description="Wait what?",
                                        landing="physicalLanding") 

@app.route('/phobia-therapy')
def phobia():
    return render_template('phobia.html', title='Phobia Therapy',
                                        inner_title="Phobia Therapy",
                                        description="A new approach to fear",
                                        landing="phobiaLanding") 

@app.route('/therapy-dogs')
def dogs():
    return render_template('dog.html', title='Therapy Dogs',
                                        inner_title="Therapy Dogs",
                                        description="Man's Best Therapist",
                                        landing="dogLanding") 

@app.route('/therapy-cats')
def cats():
    return render_template('cat.html', title='Therapy Cats',
                                        inner_title="Therapy Cats",
                                        description="Feline Finesse",
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
                                        description="Beautiful Lil' Souls",
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
                                        description="Release Endorphins",
                                        landing="petLanding")                                        

@app.route('/urgent-care')
def urgent():
    return render_template('urgent.html', title='Urgent Care',
                                        inner_title="Urgent Care",
                                        description="24/7",
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
                                        description="Feel like a man again",
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
                                        description="Redefining Women",
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
                                        description="Get back out there",
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
                                        description="Developing the Youth",
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
                                        description="Saving Relationships",
                                        landing="coupleLanding")

@app.route('/family-therapy')
def family():
    return render_template('family.html', title="Family Therapy",
                                        inner_title="Family Therapy",
                                        description="Strengthening Households",
                                        landing="familyLanding")  

@app.route('/speech-therapy')
def speech():
    return render_template('speech.html', title="Speech Therapy",
                                        inner_title="Speech Therapy",
                                        description="Learn to Love to Speak",
                                        landing="speechLanding")  

@app.route('/occupational-therapy')
def occupational():
    return render_template('occupational.html', title="Occupational Therapy",
                                        inner_title="Occupational Therapy",
                                        description="Adapt and Surpass",
                                        landing="occupationalLanding")        

@app.route('/covid-19-testing')
def covid_19():
    return render_template('covid.html', title="COVID-19 Testing",
                                        inner_title="COVID-19 Testing",
                                        description="Certainty in the midst of uncertainty",
                                        landing="covidLanding")  

@app.route('/covid-19-screening-and-treatment')
def screening():
    return render_template('screening.html', title="COVID-19 Screening and Treatment",
                                        inner_title="COVID-19 Screening and Treatment",
                                        description="Get Well Soon",
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
def our_app():
    return render_template('app.html', title="Our App",
                                        inner_title="Our App",
                                        description="Insert Text",
                                        landing="appLanding") 

@app.route('/reviews')
def reviews():
    reviews = posts.post
    page = 0
    specific_reviews = reviews[0:5]
    total_pages = math.ceil(len(reviews) / 5) # total number of pages
    return render_template('reviews.html', title="Reviews",
                                        inner_title="Reviews",
                                        description="Insert Text",
                                        landing="reviewLanding",
                                        reviews=specific_reviews,
                                        current_page=page,
                                        total_pages=total_pages) 

@app.route('/reviews/page<int:page>')
def reviews_pagination(page):
    page = page - 1
    reviews = posts.post
    start = page * 5  # starting index for the list of reviews
    end = start + 5 # ending index for the list of reviews
    specific_reviews = reviews[start:end] # getting the specific reviews for that page

    last = False
    total_pages = math.ceil(len(reviews) / 5) # total number of pages
    if (page == (total_pages - 1)): # if the page is the last page
        last = True # set last to true
    
    

    if (page <= 0):
        return redirect(url_for('reviews'))
    elif (page < total_pages): 
        return render_template('reviews_page.html', title="Reviews",
                                            inner_title="Reviews",
                                            description="Insert Text",
                                            landing="reviewLanding",
                                            total_pages=total_pages,
                                            reviews=specific_reviews,
                                            current_page=page,
                                            last=last) 
    else:
        return redirect(url_for('reviews'))


@app.route('/reviews/filtered/<int:rating>/page<int:page>')
def reviews_filtered(page, rating):
    page = page - 1
    reviews = posts.post
    start = page * 5  # starting index for the list of reviews
    end = start + 5 # ending index for the list of reviews
    specific_reviews = []
    for i in reviews:
        if (i["rating"] == rating):
            specific_reviews.append(i) 

    start = page * 5  # starting index for the list of reviews
    end = start + 5 # ending index for the list of reviews
    filtered_reviews = specific_reviews[start:end]
    
    last = False
    total_pages = math.ceil(len(specific_reviews) / 5) # total number of pages
    if (page == (total_pages - 1)): # if the page is the last page
        last = True # set last to true
    
    return render_template('reviews_page_filtered.html', title="Reviews",
                                        inner_title="Reviews",
                                        description="Insert Text",
                                        landing="reviewLanding",
                                        total_pages=total_pages,
                                        reviews=filtered_reviews,
                                        current_page=page,
                                        last=last,
                                        rating=rating) 

@app.route('/organizations')
def organizations():
    return render_template('organizations.html', title="Organizations",
                                        inner_title="Organizations",
                                        description="Insert Text",
                                        landing="organizationLanding") 
    
@app.route('/employer-groups')
def employer():
    return render_template('employer.html', title="Employer Groups",
                                        inner_title="Employer Groups",
                                        description="Insert Text",
                                        landing="employerLanding") 

@app.route('/hospitals-and-health-systems')
def hospitals():
    return render_template('hospitals.html', title="Hospitals and Health Systems",
                                        inner_title="Hospitals and Health Systems",
                                        description="Insert Text",
                                        landing="hospitalLanding") 

@app.route('/unions-and-associations')
def unions():
    return render_template('unions.html', title="Unions and Associations",
                                        inner_title="Unions and Associations",
                                        description="Insert Text",
                                        landing="unionLanding") 

@app.route('/government-and-education')
def government():
    return render_template('government.html', title="Government and Education",
                                        inner_title="Government and Education",
                                        description="Insert Text",
                                        landing="govLanding") 

@app.route('/brokers-and-advisors')
def brokers():
    return render_template('brokers.html', title="Brokers and Advisors",
                                        inner_title="Brokers and Advisors",
                                        description="Insert Text",
                                        landing="brokerLanding") 
                                        
@app.route('/distribution-partners')
def distribution():
    return render_template('distribution.html', title="Distribution Partners",
                                        inner_title="Distribution Partners",
                                        description="Insert Text",
                                        landing="distributionLanding") 

@app.route('/news')
def news():
    news_list = news_articles.news
    page = 0
    specific_news = news_list[0:12]
    total_pages = math.ceil(len(news_list) / 12)
    return render_template('news.html', title="News",
                                        inner_title="News",
                                        description="Insert Text",
                                        landing="newsLanding",
                                        news=specific_news,
                                        current_page=page,
                                        total_pages=total_pages) 

@app.route('/news/page<int:page>')
def news_pagination(page):
    news_list = news_articles.news
    page = page - 1
    start = page * 12
    end = start + 12
    specific_news = news_list[start:end]

    last = False
    total_pages = math.ceil(len(news_list) / 12) # total number of pages
    if (page == (total_pages - 1)):
        last = True
    
    if (page <= 0):
        return redirect(url_for('news'))
    elif (page < total_pages):
        return render_template('news_page.html', title="News",
                                        inner_title="News",
                                        description="Insert Text",
                                        landing="newsLanding",
                                        total_pages=total_pages,
                                        news=specific_news,
                                        current_page=page,
                                        last=last) 
    else:
        return redirect(url_for('news'))

@app.route('/news/article/<article_link>')
def news_article(article_link):
    news_list = news_articles.news
    actual_news = []
    for i in news_list:
        if (i["link"] == article_link):
            actual_news.append(i)
    if not actual_news:
        return redirect(url_for('news'))
    return render_template('news_article.html', title="News",
                                        inner_title="News",
                                        description="Insert Text",
                                        landing="newsLanding",
                                        article=actual_news)


@app.route('/blog')
def blog():
    news_list = blog_articles.blogs
    page = 0
    specific_news = news_list[0:12]
    total_pages = math.ceil(len(news_list) / 12)
    return render_template('blog.html', title="Blog",
                                        inner_title="Blog",
                                        description="Insert Text",
                                        landing="blogLanding",
                                        news=specific_news,
                                        current_page=page,
                                        total_pages=total_pages) 

@app.route('/blog/page<int:page>')
def blog_pagination(page):
    news_list = blog_articles.blogs
    page = page - 1
    start = page * 12
    end = start + 12
    specific_news = news_list[start:end]

    last = False
    total_pages = math.ceil(len(news_list) / 12) # total number of pages
    if (page == (total_pages - 1)):
        last = True
    
    if (page <= 0):
        return redirect(url_for('blog'))
    elif (page < total_pages):
        return render_template('blog_page.html', title="Blog",
                                        inner_title="Blog",
                                        description="Insert Text",
                                        landing="blogLanding",
                                        total_pages=total_pages,
                                        news=specific_news,
                                        current_page=page,
                                        last=last) 
    else:
        return redirect(url_for('blog'))

@app.route('/blog/article/<article_link>')
def blog_article(article_link):
    news_list = blog_articles.blogs
    blogs_recent = news_list[0:3]
    actual_news = []
    for i in news_list:
        if (i["link"] == article_link):
            actual_news.append(i)
    if not actual_news:
        return redirect(url_for('blog'))
    return render_template('blog_article.html', title="Blog",
                                        inner_title="Blog",
                                        description="Insert Text",
                                        landing="blogLanding",
                                        article=actual_news,
                                        blogs=blogs_recent)

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact",
                                        inner_title="Contact",
                                        description="Insert Text",
                                        landing="contactLanding") 

@app.route('/faq')
def faq():
    return render_template('faq.html', title="FAQ",
                                        inner_title="FAQ",
                                        description="Insert Text",
                                        landing="faqLanding") 

@app.route('/our-social')
def social():
    return render_template('social.html', title="Our Social",
                                        inner_title="Our Social",
                                        description="Insert Text",
                                        landing="socialLanding") 

@app.route('/join-us')
def join():
    return render_template('join.html', title="Join Us",
                                        inner_title="Join Us",
                                        description="Insert Text",
                                        landing="joinLanding") 


# login route
@app.route('/login', methods=['GET', 'POST']) # methods arguments tells Flask that the function accepts GET and POST requests, default is only GET
def login():
    if current_user.is_authenticated: # if a logged in user goes to the login page, they will be redirected to the homepage
        return redirect(url_for('dashboard', username=current_user.username))
    form = LoginForm() 
    if form.validate_on_submit(): # when the browser sends the GET request to receive the webpage with the form, the method is going to return false, skipping to the redirect line
        user = User.query.filter_by(username=form.username.data).first() # loading the user from the database
        if user is None or not user.check_password(form.password.data): # checking whether the user's password or username is invalid
            flash ('Invalid username or password', 'error')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data) # if both username and password are correct, then call the login_user function which comes with Flask-Login, meaning that any future pages the user navogates to will ave the current_user set to that uesr
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard', username=current_user.username)
        return redirect(next_page) 
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                                                first_name=form.first_name.data,
                                                last_name=form.last_name.data,
                                                phone=form.phone.data,
                                                gender=form.gender.data,
                                                birthday=form.datepicker.data,
                                                address=form.address.data,
                                                city=form.city.data,
                                                state=form.state.data,
                                                zip_code=form.zip_code.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'info')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/database')
def database():
    user_all = User.query.all()
    appointments_all = Appointments.query.all()
    allergies_all = Allergies.query.all()
    surgeries_all = Surgeries.query.all()
    conditions_all = Conditions.query.all()
    return render_template('database.html', title='Database', 
                                            user_all=user_all,
                                            appointments_all=appointments_all,
                                            allergies_all=allergies_all,
                                            surgeries_all=surgeries_all,
                                            conditions_all=conditions_all)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password', 'info')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                            title='Request Password Reset',
                            form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset', 'info')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form, title="Reset Password")

# User dashboard
@app.route('/<username>/dashboard')
@login_required
def dashboard(username):
    user_actual = User.query.filter_by(username=username).first()
    user_appointments = Appointments.query.filter_by(user_id=user_actual.id).filter(Appointments.start_time>datetime.utcnow()).order_by(Appointments.start_time.asc()).all()
    scheduled = False
    print(user_appointments)
    if len(user_appointments) != 0: 
        scheduled = True
    return render_template('dashboard.html', title='Patient Dashboard', user=user_actual,
                                                                        user_appointments=user_appointments,
                                                                        scheduled=scheduled)

@app.route('/<username>/schedule-appointment', methods=['GET', 'POST'])
@login_required
def schedule_appointment(username):
    user = User.query.filter_by(username=username).first()
    form = MakeAppointmentForm()
    user_appointments = Appointments.query.filter_by(user_id=user.id).all()
    if form.validate_on_submit():

        date = form.datepicker.data

        description = form.description.data
        doctor = form.doctor.data
        hour = form.hour.data
        minute = form.minute.data
        duration = form.duration.data

        stringdate = datetime(date.year, date.month, date.day)
        newdatetime = stringdate.replace(date.year, date.month, date.day, hour, minute)

        
        minutes_added = timedelta(minutes=duration)
        future_time = newdatetime + minutes_added

        if user_appointments is not None:
            for u in user_appointments:
                if u.start_time == newdatetime:
                    flash('You have already scheduled an appointment at this time', 'error')
                    return redirect(url_for('schedule_appointment', username=username))
        
        # adding the appointment
        a = Appointments(user_id=user.id, start_time=newdatetime, end_time=future_time, description=description, doctor=doctor)
        print("HELLO")
        db.session.add(a)
        db.session.commit()
        send_appointment_email(user, a)
        flash('Appointment successfully scheduled. Please check your email.', 'info')
        return redirect(url_for('dashboard', username=username))
    return render_template('make_appointment.html', title='Schedule Appointment',
                                                    form=form, 
                                                    user=user)

@app.route('/<username>/appointments')
@login_required
def appointments(username):
    user = User.query.filter_by(username=username).first()
    appointments = Appointments.query.filter_by(user_id=user.id).order_by(Appointments.start_time.asc()).all() # getting the user's appointments from most recent
    return render_template('appointments.html', title="Appointments", user=user,
                                                                    appointments=appointments)

@app.route('/<username>/appointments/<appointment_id>')
@login_required
def appointments_specific(username, appointment_id):
    user = User.query.filter_by(username=username).first()
    appointment = Appointments.query.get(appointment_id)

    return render_template('appointments_specific.html', title='Appointment Information', user=user,
                                                                                        appointment=appointment)

@app.route('/<username>/my-account', methods=['GET', 'POST'])
@login_required
def user_account(username):
    user = User.query.filter_by(username=username).first()
    form = UserAccount()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.phone = form.phone.data
        user.gender = form.gender.data 
        user.address = form.address.data
        user.city = form.city.data 
        user.state = form.state.data
        user.zip_code = form.zip_code.data
        
        db.session.commit()
        flash('Your changes have been saved', 'info')
    elif request.method == 'GET':
        form.username.data = user.username 
        form.email.data = user.email
        form.first_name.data = user.first_name
        form.last_name.data = user.last_name
        form.phone.data = user.phone
        form.gender.data = user.gender
        form.address.data = user.address
        form.city.data = user.city
        form.state.data = user.state
        form.zip_code.data = user.zip_code
    else:
        flash('There are errors in your changes', 'error')
    return render_template('user_account.html', title='My Account', user=user, 
                                                                    form=form)

@app.route('/<username>/health-profile', methods=['GET', 'POST'])
@login_required
def health_profile(username):
    user = User.query.filter_by(username=username).first()
    allergies = Allergies.query.filter_by(user_id=user.id)
    form = AllergyForm()
    if form.validate_on_submit():
        if allergies is not None:
            for a in allergies:
                if a.allergy == form.allergy.data.capitalize():
                    flash('You already have "' + a.allergy + '" listed as an allergen', 'error')
                    return redirect(url_for('health_profile', username=username))
        user_allergy = Allergies(user_id=user.id, allergy=form.allergy.data.capitalize())
        db.session.add(user_allergy)
        db.session.commit()
        flash('Your changes have been updated', 'info')

    surgeries = Surgeries.query.filter_by(user_id=user.id)
    surgery_form = SurgeryForm()
    if surgery_form.validate_on_submit():
        if surgeries is not None:
            for s in surgeries:
                if s.surgery == surgery_form.surgery.data.capitalize():
                    flash('You already have "' + s.surgery + '" listed as a surgery', 'error')
                    return redirect(url_for('health_profile', username=username))
        user_surgery = Surgeries(user_id=user.id, surgery=surgery_form.surgery.data.capitalize())
        db.session.add(user_surgery)
        db.session.commit()
        flash('Your changes have ben updated', 'info')

    conditions = Conditions.query.filter_by(user_id=user.id)
    condition_form = ConditionForm()
    if condition_form.validate_on_submit():
        if conditions is not None:
            for c in conditions:
                if c.condition == condition_form.condition.data.capitalize():
                    flash('You already have "' + c.condition + '" listed as a medical condition', 'error')
                    return redirect(url_for('health_profile', username=username))
        user_condition = Conditions(user_id=user.id, condition=condition_form.condition.data.capitalize())
        db.session.add(user_condition)
        db.session.commit()
        flash('Your changes have ben updated', 'info')
    
    return render_template('health_profile.html', title='Health Profile', user=user,
                                                                        allergies=allergies,
                                                                        form=form,
                                                                        surgeries=surgeries,
                                                                        surgery_form=surgery_form,
                                                                        conditions=conditions,
                                                                        condition_form=condition_form)
                                                        

# # Edit Profile function
# @app.route('/edit_profile', methods=['GET', 'POST'])
# @login_required
# def edit_profile():
#     form = EditProfileForm()
#     if form.validate_on_submit(): # If the form successfully submitted
#         current_user.username = form.username.data # Set the user's username to what they entered in the form
#         current_user.about_me = form.about_me.data # Set about me for current user to input from the form
#         db.session.commit() # Commit changes to the database
#         flash('Your changes have been saved', 'info')
#         return redirect(url_for('user', username=current_user.username))
#     elif request.method == 'GET': # If this is the first time that the form has been requested
#         form.username.data = current_user.username # Then pre-populate the fields with the data in the database
#         form.about_me.data = current_user.about_me
#     return render_template('edit_profile.html', form=form, title="Edit Profile")
