import lab5b

def test_pixel_constrait():
    """ 
    Declares the test function and then test a normal function, 
    then it tests if every hsv is wrong followed by hue wrong,
    saturation wrong and lastly value wrong.
    """
    test_function = lab5b.pixel_constraint(50, 70, 50, 70, 50, 70)
    assert test_function((60, 60, 60)) == 1
    assert test_function((80, 80, 80)) == 0
    assert test_function((80, 60, 60)) == 0 
    assert test_function((60, 80, 60)) == 0
    assert test_function((60, 60, 80)) == 0
    print ("All tests worked for pixel_constraint")

def test_generator_from_image():
    """ Declares the test function and then test two normal functions """
    test_function = lab5b.generator_from_image([(50,60,10), (10,23,50), (34, 50, 60), (60, 50, 40)])
    assert test_function(1) == (10, 23, 50)
    assert test_function(3) == (60, 50, 40)
    print ("All tests worked for generator_from_image")

def test_combine_images():
    """ 
    Creates a fake image with fake tuples, also the generator is generating from our fake images. 
    Then it test with the value 0.5 there it should use both generator 1 and 2, 
    then we test generator 1 and lastly we test only generator 2
    """
    fake_img = [(21,21,21), (21, 21, 21)]
    second_fake_img = [(12, 12, 12), (12, 12, 12)]
    hsv_list = [(1, 1, 1), (1, 1, 1)]
    generator1 = lab5b.generator_from_image(fake_img)
    generator2 = lab5b.generator_from_image(second_fake_img)

    test_function_first = lab5b.combine_images(hsv_list, first_constant_condition, generator1, generator2)
    assert test_function_first == [(16.5, 16.5, 16.5), (16.5, 16.5, 16.5)]
    test_function_second = lab5b.combine_images(hsv_list, second_constant_condition, generator1, generator2)
    assert test_function_second == [(21, 21, 21), (21, 21, 21)]
    test_function_third = lab5b.combine_images(hsv_list, third_constant_condition, generator1, generator2)
    assert test_function_third == [(12, 12, 12), (12, 12, 12)]
    print("All tests worked for combine_images")

def first_constant_condition(bgr):
    """ Always returns 0.5 """
    return 0.5

def second_constant_condition(bgr):
    """ Always returns 1 """
    return 1

def third_constant_condition(bgr):
    """ Always returns 0 """
    return 0

if __name__ == "__main__":
    test_pixel_constrait()
    test_generator_from_image()
    test_combine_images()