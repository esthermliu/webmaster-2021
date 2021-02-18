from flask import render_template, flash, redirect, url_for, request
from app import app, posts, news_articles, blog_articles, login
from app import db
from app.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from app.models import User
from flask_login import logout_user, login_required
from flask_login import current_user, login_user
from werkzeug.urls import url_parse
import math
from flaskext.markdown import Markdown
from app.email import send_password_reset_email

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
        return redirect(url_for('index'))
    form = LoginForm() 
    if form.validate_on_submit(): # when the browser sends the GET request to receive the webpage with the form, the method is going to return false, skipping to the redirect line
        user = User.query.filter_by(username=form.username.data).first() # loading the user from the database
        if user is None or not user.check_password(form.password.data): # checking whether the user's password or username is invalid
            flash ('Invalid username or password', 'error')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data) # if both username and password are correct, then call the login_user function which comes with Flask-Login, meaning that any future pages the user navogates to will ave the current_user set to that uesr
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
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
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'info')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/database')
def database():
    user_all = User.query.all()
    return render_template('database.html', title='Database', user_all=user_all)

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
                            title='Reset Password',
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
    return render_template('reset_password.html', form=form)

