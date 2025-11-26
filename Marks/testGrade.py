import grade

def test_val_marks():
    assert validate_marks(67)==67
    assert validate_marks(10000)== False
    assert validate_marks(100)== 100

def test_val_students():
    assert validate_students(2) == 2
    assert validate_students(20) == 20
    assert validate_students(200) == False
    
def test_get_grade():
    assert get_grade(55)== 5
    assert get_grade(96)== 9
    assert get_grade(0)== "U"

test_val_marks()
test_val_students()
test_get_grade()
