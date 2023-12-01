from django.test import SimpleTestCase

# Create your tests here.
class TestHeyYou(SimpleTestCase):
    def test_hey_nate(self):
        response = self.client.get("/function/hey/?input_name=Nate")
        self.assertContains(response, "Hey, Nate!")

    def test_hey_bcca(self):
        response = self.client.get("/function/hey/?input_name=BCCA")
        self.assertContains(response, "Hey, BCCA!")

class TestAgeIn(SimpleTestCase):
    def test_age_in_2050_born_2000(self):
        response = self.client.get("/function/age_in_2050/?birthyear=2000&ageyear=2050")
        self.assertContains(response, "50")

    def test_age_in_2050_born_0(self):
        response = self.client.get("/function/age_in_2050/?birthyear=0&ageyear=2050")
        self.assertContains(response, "2050")

    def test_age_in_2010_born_1995(self):
        response = self.client.get("/function/age_in_2050/?birthyear=1995&ageyear=2010")
        self.assertContains(response, "15")

    def test_age_in_1950_born_1920(self):
        response = self.client.get("/function/age_in_2050/?birthyear=1920&ageyear=1950")
        self.assertContains(response, "30")


class TestOrderTotal(SimpleTestCase):
    def test_order_total_0_0_0(self):
        response = self.client.get("/function/order/?Burger=0&Fries=0&Drink=0")
        self.assertContains(response, "0.0")

    def test_order_total_1_1_1(self):
        response = self.client.get("/function/order/?Burger=1&Fries=1&Drink=1")
        self.assertContains(response, "7.0")

    def test_order_total_2_3_4(self):
        response = self.client.get("/function/order/?Burger=2&Fries=3&Drink=4")
        self.assertContains(response, "17.5")

    def test_order_total_4_3_2(self):
        response = self.client.get("/function/order/?Burger=4&Fries=3&Drink=2")
        self.assertContains(response, "24.5")


class TestFontTimes(SimpleTestCase):
    def test_Chocolate_2(self):
        response = self.client.get("/codinghub/warmup-2/font-times/?str_1=Chocolate&num_1=2")
        self.assertContains(response, "ChoCho")

    def test_Chocolate_3(self):
        response = self.client.get("/codinghub/warmup-2/font-times/?str_1=Chocolate&num_1=3")
        self.assertContains(response, "ChoChoCho")

    def test_ABC_3(self):
        response = self.client.get("/codinghub/warmup-2/font-times/?str_1=Abc&num_1=3")
        self.assertContains(response, "AbcAbcAbc")

class TestNoTeenSum(SimpleTestCase):
    def test_1_2_3(self):
        response = self.client.get("/codinghub/logic-2/no-teen-sum/?int_value1=1&int_value2=2&int_value3=3")
        self.assertContains(response, "6")

    def test_1_2_3(self):
        response = self.client.get("/codinghub/logic-2/no-teen-sum/?int_value1=2&int_value2=13&int_value3=1")
        self.assertContains(response, "3")

    def test_1_2_3(self):
        response = self.client.get("/codinghub/logic-2/no-teen-sum/?int_value1=2&int_value2=1&int_value3=14")
        self.assertContains(response, "3")

    
class TestXYZ(SimpleTestCase):
    def test_abcxyz(self):
        response = self.client.get("/codinghub/string-2/xyz-there?xyz_string=abcxyz")
        self.assertContains(response, "True")

    def test_abc_xyz(self):
        response = self.client.get("/codinghub/string-2/xyz-there?xyz_string=abc.xyz")
        self.assertContains(response, "False")

    def test_xyz_abc(self):
        response = self.client.get("/codinghub/string-2/xyz-there?xyz_string=xyz.abc")
        self.assertContains(response, "True")
    
class TestCenteredAverage(SimpleTestCase):
    def test_1_through_10(self):
        response = self.client.get("/codinghub/list-2/centered-average?val_1=1&val_2=2&val_3=3&val_4=4&val_5=100&val_6=&val_7=")
        self.assertContains(response, "3")

    def test_1_1_5_5_10_8_7(self):
        response = self.client.get("/codinghub/list-2/centered-average?val_1=1&val_2=1&val_3=5&val_4=5&val_5=10&val_6=8&val_7=7")
        self.assertContains(response, "5")

    def test_10_4_2_4_2_0(self):
        response = self.client.get("/codinghub/list-2/centered-average?val_1=-10&val_2=-4&val_3=-2&val_4=-4&val_5=-2&val_6=0&val_7=")
        self.assertContains(response, "-3")