# Write a program in python,to open a browser window and open "youtube.com" and output the name of first video.
# driver.get

from selenium import webdriver
import selenium
driver = webdriver.chrome()
driver.get("https://www.youtube.com/watch?v=UDpo7StAvpw")

