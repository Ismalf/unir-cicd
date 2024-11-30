import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator
from app.calc import InvalidPermissions


def mocked_validation(*args, **kwargs):
    return True

def mocked_validation_negative(*args, **kwargs):
    return False


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # ===================================================================== add tests
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
    
    # ===================================================================== Test substract function
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(self.calc.substract(10, 5), 5)
        self.assertEqual(self.calc.substract(-1, -1), 0)
        self.assertEqual(self.calc.substract(2, -2), 4)
        self.assertEqual(self.calc.substract(-1, 1), -2)

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    # ================================================================================================ multiplication tests
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0.0, self.calc.multiply(1.0, 0.0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertEqual(2, self.calc.multiply(-1, -2))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_fails_with_nan_parameter(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    @patch('app.util.validate_permissions', side_effect=mocked_validation_negative, create=True)
    def test_multiply_method_returns_correct_result_fails_validation(self, _validate_permissions):
        self.assertRaises(InvalidPermissions, self.calc.multiply, 2, 2)
        self.assertRaises(InvalidPermissions, self.calc.multiply, 1, 0)
        self.assertRaises(InvalidPermissions, self.calc.multiply, -1, 0)
        self.assertRaises(InvalidPermissions,  self.calc.multiply, -1, 2)

    # =============================================================================================== divisions tests
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(0.25, self.calc.divide(1, 4))
        self.assertEqual(-1, self.calc.divide(-4, 4))
        self.assertEqual(2, self.calc.divide(-4, -2))
        self.assertEqual(-2, self.calc.divide(4, -2))


    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, 2, object())
        self.assertRaises(TypeError, self.calc.divide, object(), object())
        self.assertRaises(TypeError, self.calc.divide, object(), 2)

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    # ===================================================================== power tests
    def test_power_method_returns_correct_result(self):
        self.assertEqual(self.calc.power(2.0, 3.0), 8.0)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(2, -2), 0.25)
        self.assertEqual(self.calc.power(0, 0), 1)
        self.assertEqual(self.calc.power(10, 1), 10)
    
    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "0", 0)
        self.assertRaises(TypeError, self.calc.power, 1, "0")
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, object(), object())
        

    # ===================================================================== square root tests
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(self.calc.sqrt(4), 2)
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(0), 0)
        self.assertEqual(self.calc.sqrt(0.25), 0.5)

    def test_sqrt_method_fails_with_math_error(self):
        self.assertRaises(TypeError, self.calc.sqrt, -4)
        self.assertRaises(TypeError, self.calc.sqrt, -1000)


    def test_sqrt_method_fails_with_nan(self):
        self.assertRaises(TypeError, self.calc.sqrt, "-1000")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())

    # ===================================================================== log10 tests
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(self.calc.log10(100), 2)
        self.assertEqual(self.calc.log10(1), 0)
        self.assertEqual(self.calc.log10(10), 1)
        self.assertEqual(self.calc.log10(0.1), -1)

    def test_log10_method_fails_with_math_error(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -0.00001)

    def test_log10_method_fails_with_nan(self):
        self.assertRaises(TypeError, self.calc.log10, "-0.00001")
        self.assertRaises(TypeError, self.calc.log10, object())
        self.assertRaises(TypeError, self.calc.log10, None)

    # ===================================================================== Test check_types 
    def test_check_types_fails_with_nan(self):
        self.assertRaises(TypeError, self.calc.check_types, "string", 5)
        self.assertRaises(TypeError, self.calc.check_types, 1, "5")
        self.assertRaises(TypeError, self.calc.check_types, "1", "5")
    
    def test_check_types_success(self):
        self.assertEqual(self.calc.check_types(0.1, 1), None)
        self.assertEqual(self.calc.check_types(0.1, 1.1), None)
        self.assertEqual(self.calc.check_types(0, 1.1), None)
        self.assertEqual(self.calc.check_types(0, 1), None)
        
        


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
