import math_func
import pytest
import sys 

# dont forget to write 'test' keyword in test function and file name as pytest module will not be able to recognise test cases and testable files
# however we can change the file name but we need to change the filename in command prompt according to it


@pytest.mark.skip(reason="do not test add function") #to skip a particular testcase with reason
@pytest.mark.skipif(sys.version_info<(3,3) , reason="do not test add function") #to skip a particular testcase having condition with reason
# @pytest.mark.skipif(sys.version_info>(3,3) , reason="do not test add function") #to skip a particular testcase having condition with reason
@pytest.mark.number #to execute particular test cases using mark name
def test_add(): 
	assert math_func.add(7,3)==10
	assert math_func.add(7)==9
	assert math_func.add(7)!=1
	assert math_func.add(7)>8
	assert math_func.add(7)<10
	assert math_func.add(7)<=9
	assert math_func.add(7)>=9
	



@pytest.mark.number
def test_product():
	assert math_func.product(5,5)==25
	assert math_func.product(5)==10
	assert math_func.product(7)!=1
	assert math_func.product(7)>10
	assert math_func.product(7)<15
	assert math_func.product(7)<=14
	assert math_func.product(7)>=14
	print(math_func.product(7,3),'----------------------------')




@pytest.mark.string
def test_add_string():
	assert math_func.add('Hello','world')=='Helloworld'
	assert type(math_func.add('Hello','world')) is str
	assert 'Heldlo' not in math_func.add('Hello','world')




@pytest.mark.string
def test_product_string():
	assert math_func.product('Hello',3)=='HelloHelloHello'
	assert math_func.product('Hello')=='HelloHello'
	assert 'Hello' in math_func.product('Hello',1)