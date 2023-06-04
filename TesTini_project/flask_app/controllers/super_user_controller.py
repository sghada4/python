import random
from flask_app import app
from flask import render_template,request, redirect, session,flash
from flask_app.models.group_model import Group
from flask_app.models.module_model import Module
from flask_app.models.test_model import Test
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#* ***********Display Route***********
@app.route('/')
def register():
    return render_template('sign-up.html')

#* ***********Action Route***********
@app.route('/users/register', methods=['post'])
def sign_up():
    if not User.validate_user(request.form):
        return redirect('/')

    data={
        **request.form,
        'password':bcrypt.generate_password_hash(request.form['password'])
    }
    user=User.save_user(data)
    session['user_id']=user
    return redirect('/sign_in')

#* ***********Action Route***********
#Login user with validate form
@app.route('/users/login',methods=['POST'])
def login():
    user_db = User.get_by_email(request.form)
    if  not user_db:
        flash('Invalid email or password',"login")
        return redirect('/sign_in')
    elif not bcrypt.check_password_hash(user_db.password, request.form['password']):
        flash('Invalid email or password',"login")
        return redirect('/sign_in')
    elif user_db.role=="owner":
        session['super_user_id']=user_db.id
        return redirect('/dashboard_super_user')

    session['user_id']=user_db.id
    return redirect('/dashboard_user')

#* ***********Display Route***********
@app.route('/sign_in')
def sign_in():
    return render_template('sign-in.html')


#* ***********Display Route***********
@app.route('/dashboard_super_user')
def dashboard_super_user():
    data={'user_id':session['super_user_id'],'id':session['super_user_id']}
    all_super_user_groups=Group.get_users_groups_limit(data)
    user=User.get_by_id(data)
    num=Group.get_users_groups_num(data)
    num1=Group.get_other_groups_num(data)
    all_other_groups=Group.get_others_groups_limit(data)
    return render_template('dashboard_super_user.html',all_super_user_groups=all_super_user_groups,user=user,all_other_groups=all_other_groups,num=num,num1=num1)
    
#* ***********Display Route***********

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/sign_in')

#* ***********Action Route***********
@app.route('/profile')
def profile_super_user():
    user=User.get_by_id({'id':session['super_user_id']})
    return render_template('profile.html',user=user)


#* ***********Display Route***********
@app.route('/test')
def test():
    return render_template('test.html')




@app.route('/create_new_group')
def create_new_group():
    return render_template('create_new_group.html')

@app.route('/created_groups')
def created_groups():
    data={'user_id':session['super_user_id']}
    all_super_user_groups=Group.get_users_groups(data)
    return render_template('created_groups.html',all_super_user_groups=all_super_user_groups)

@app.route('/other_groups')
def other_groups_super_user():
    all_other_groups=Group.get_others_groups_super_user({'user_id':session['super_user_id']})
    return render_template('other_groups_super_user.html',all_other_groups=all_other_groups)

@app.route('/save_new_group' ,methods=['POST'])
def save_new_group():
    
    if not Group.validate_group(request.form):
        return redirect('/create_new_group')

    data={
        **request.form,
        'user_id':session['super_user_id']
    }
    group_id=Group.save_group(data)

    return redirect('/created_groups')

@app.route('/delete_group/<int:id>')
def delete_group(id):
    data={'id':id}
    Group.delete_group(data)

    return redirect('/dashboard_super_user')



@app.route('/delete_group1/<int:id>')
def delete_group1(id):
    data={'id':id}
    Group.delete_group(data)

    return redirect('/created_groups')





@app.route('/edit_group' ,methods=['POST'])
def edit_group():

    if not Group.validate_group(request.form):
        return redirect('/edit_new_group/<int:id>')

    # data={
    #     **request.form
    # }
    Group.update_group(request.form)

    return redirect('/created_groups')

@app.route('/edit_new_group/<int:id>')
def edit_group_page(id):
    data={'id':id}
    group=Group.get_by_id_group(data)
    # session['group_id']=id
    return render_template('edit_group.html',group=group)








#* ***********Display Route***********
@app.route('/dashboard_user')
def dashboard_user():
    user = User.get_by_id({'id': session['user_id']})
    all_modules=Module.get_all_modules()
    other_groups=Group.get_others_groups_user({'user_id': session['user_id']})
    my_groups=Group.joined_groups({'user_id': session['user_id']})
    num=Group.joined_groups_num({'user_id': session['user_id']})
    num1=Group.other_groups_num({'user_id': session['user_id']})
    return render_template('dashboard_user.html', user=user, all_modules=all_modules,other_groups=other_groups, my_groups=my_groups,num=num,num1=num1)

#* ***********Action Route***********
@app.route('/cancel/<int:joined_group>')
def cancel(joined_group):
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    Group.cancel_group({'user_id':session['user_id'], 'group_id':joined_group})
    return redirect('/dashboard_user')

#* ***********Action Route***********
@app.route('/joined/<int:other_groups>')
def join(other_groups):
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    if not Group.one_joined_group({'user_id':session['user_id'], 'group_id':other_groups}):
        Group.join_group({'user_id':session['user_id'], 'group_id':other_groups})
    return redirect('/dashboard_user')

    


#* ***********Display Route***********
@app.route('/modules')
def modules():
    user=User.get_by_id({'id':session['user_id']})
    all_modules=Module.get_all_modules()
    my_tests=User.get_all_tests_user({'id': session['user_id']})

    return render_template('list_modules.html',user=user, all_modules=all_modules,my_tests=my_tests)

#* ***********Display Route***********
@app.route('/joined_groups')
def my_groups():
    my_groups=Group.joined_groups({'user_id': session['user_id']})
    return render_template('joined_groups.html',my_groups=my_groups)

#* ***********Display Route***********
@app.route('/ancient_result')
def result():
    random_num = random.randint(1, 4)
    return render_template(f'result{random_num}.html')

#* ***********Display Route***********


#* ***********Display Route***********
@app.route('/my_tests')
def my_tests():
    user = User.get_by_id({'id': session['user_id']})
    my_tests=User.get_all_tests_user({'id': session['user_id']})
    return render_template('ancient_tests.html', user=user, my_tests=my_tests)

#* ***********Display Route***********
@app.route('/other_groups_user')
def other_groups():
    other_groups=Group.get_others_groups_user({'user_id': session['user_id']})

    return render_template('other_groups_user.html', other_groups=other_groups)

#* ***********Display Route***********
@app.route('/take_test/<int:id>')
def module(id):
    module=Module.get_by_id({'id':id})
    all_tests=Test.get_test_by_module({'module_id':id})
    return render_template('take_test.html',module=module,all_tests=all_tests)

#* ***********Action Route***********
@app.route('/take_test', methods=['post'])
def take_test():
    id=request.form['id']
    return redirect(f'/final_test/{id}')

#* ***********Display Route***********
@app.route('/final_test/<int:id>')
def final_test(id):
    
    return render_template(f'test{id}.html')

#* ***********Display Route***********
@app.route('/group_details/<int:id>')
def group_details(id):
    
    return render_template('group_list_user.html')



@app.route('/group_list/<int:id>')
def group_list(id):
    data={'id':id}
    group=Group.get_by_id_group(data)
    # module=Module.get_info_one_group(data)
    return render_template('group_list_super_user.html',group=group)




