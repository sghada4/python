from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.trip_model import Trip
from flask_app.models.user_model import User

#* ***********Display Route***********
@app.route('/trips/new')
def trip_form():
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    user = User.get_by_id({'id':session['user_id']})
    return render_template('create_trip.html',user=user)

#* ***********Action Route***********
@app.route('/trips/create', methods=['post'])
def create_trip():
    if not Trip.validate_trip(request.form):
        return redirect('/trips/new')
    trip_data={
        **request.form,
        'user_id': session['user_id']
    }
    Trip.save_trip(trip_data)
    return redirect('/dashboard')

#* ***********Display Route***********
@app.route('/trips/<int:trip_id>')
def show_trip(trip_id):
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    trip=Trip.get_by_id_trip({'id':trip_id})
    user = User.get_by_id({'id':session['user_id']})
    joined_people=User.people_joined_trip({'trip_id':trip_id})
    return render_template('show_trip.html',trip=trip,user=user, joined_people=joined_people)

#* ***********Display Route***********
@app.route('/trips/edit/<int:trip_id>')
def edit_trip(trip_id):
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    trip= Trip.get_by_id_trip({'id': trip_id})
    session['trip_id']= trip_id
    user = User.get_by_id({'id':session['user_id']})
    return render_template('edit_trip.html',trip=trip, user=user)

#* ***********Action Route***********
@app.route('/trips/edit', methods=['post'])
def edit():
    if not Trip.validate_trip(request.form):
        id=session['trip_id']
        return redirect(f'/trips/edit/{id}')
    trip_data= {
        **request.form,
        'id': session['trip_id']
    }
    Trip.update_trip(trip_data)
    return redirect('/dashboard')

#* ***********Action Route***********
@app.route('/trips/delete/<int:trip_id>')
def delete(trip_id):
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    Trip.delete_trip({'id':trip_id})
    return redirect('/dashboard')

#* ***********Action Route***********
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

#* ***********Action Route***********
@app.route('/cancel/<int:joined_trip>')
def cancel(joined_trip):
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    Trip.cancel_trip({'user_id':session['user_id'], 'trip_id':joined_trip})
    return redirect('/dashboard')

#* ***********Action Route***********
@app.route('/joined/<int:peoples_trip>')
def join(peoples_trip):
    if 'user_id' not in session:#?if he has not an id redirect to the register page
        return redirect('/')
    if not Trip.one_joined_trip({'user_id':session['user_id'], 'trip_id':peoples_trip}):
        Trip.join_trip({'user_id':session['user_id'], 'trip_id':peoples_trip})
    return redirect('/dashboard')