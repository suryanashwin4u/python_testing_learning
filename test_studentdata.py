from student_data import StudentDB
import pytest
# db=None

#using fixtures
@pytest.fixture(scope='module')
def db():
	print('------------setup------------')
	db=StudentDB()
	db.connect('data.json')
	# return db
	yield db
	print('----------teardown-----------')
	db.close()

# this method is used to setup class initialization
# def setup_module(module):
# 	print('------------setup------------')
# 	global db
# 	db=StudentDB()
# 	db.connect('data.json')

# this method is used to close class initialization
# def teardown_module(module):
# 	print('----------teardown-----------')
# 	db.close()

def test_scott_data(db):
	# db=StudentDB()
	# db.connect('data.json')
	scott_data=db.get_data('Scott')
	assert scott_data['id']==1
	assert scott_data['name']=='Scott'
	assert scott_data['result']=='pass'

def test_mark_data(db):
	# db=StudentDB()
	# db.connect('data.json')
	mark_data=db.get_data('Mark')
	assert mark_data['id']==2
	assert mark_data['name']=='Mark'
	assert mark_data['result']=='fail'
