# Задаче по переименованию, немного отличается от исходного, но концепция сохраняется.
import create_files as cf
import renames as rnm

lst_ext = ['.txt', '.png', '.jpg', '.flv', '.avi', '.gif', '.mp3', '.mp4']
cf.generates(30, lst_ext, '222')
rnm.renames_files('222', '.jpg', 5)