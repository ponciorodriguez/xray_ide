from tkinter import *
from threading import Thread
import time
import winsound
import random
import os
from PIL import Image
import img_db.image_db


cwd = os.path.dirname(__file__)


kv = 40
kv_str = ("  " + "40")
kvf = 40
kvf_str = ("  " + "40")
mA = 10
mA_str = ("  " + "10")
mA_f = 0.1
sg = float(0.05)
fs = 40
ct = 0
cm = 0
puntos = 'mA'
sin_seg = 'sg'
miliseg = float()
mas_sel = 0
mAs_calc = float()
mAs = float(mA*sg)
delgado = 0
releasekvdown = True
releasekvup = True
releaseshoot = True
frequency = int()
duration = int()
estado_torax_pa = 0
estado_torax_lat = 0
estado_parrilla_costal = 0
estado_hombro = 0
estado_cervical_ap = 0
estado_s_paranasales = 0
estado_craneo_pa = 0
estado_craneo_lat = 0
estado_abdomen_simple = 0
estado_cadera_femur = 0
estado_dorsal_ap = 0
estado_dorsal_lat = 0
estado_lumbar_ap = 0
estado_lumbar_lat = 0
estado_hueso_nasal = 0
estado_sacro_lat = 0
estado_rodilla_ap = 0
estado_tibia_perone = 0
estado_tobillo_lat = 0
estado_pie_ap = 0
estado_codo_ap = 0
estado_mano_ap = 0
estado_dedos = 0
estado_muñeca = 0
contador_alarma = 0
contador_servicio = 0
t_f = 0
p_f_s = 0
text_1 = str("--------")
text_2 = str("--------")
text_3 = str("--------")
text_4 = str("--------")
text_5 = str("--------")
text_6 = str("--------")
text_7 = str("--------")
text_8 = str("--------")
sens_s_s_str = (" " + "0")
sens_s_s = 0

def sedecal():
	#seleccion kilovoltios grafia


	def click_kv_cont_up():
		global kv
		global releasekvup
		global kv_str
		releasekvup = False
		while not releasekvup:
			time.sleep(0.2)

			if kv==150:
				kv=kv
			else:
				kv= kv + 1
			if kv < 100:
				kv_str = ("  " + str(kv))
			elif kv >= 100:
				kv_str = (" " + str(kv))

			textokv.delete("1.0","end")
			textokv.insert(INSERT, (kv_str))

	def release_kv_cont_up(e):
		global releasekvup
		releasekvup = True

	def click_kv_cont_down():
		global kv
		global releasekvdown
		releasekvdown = False
		while not releasekvdown:
			time.sleep(0.2)

			if kv== 40:
				kv=kv
				
			else:
				kv=kv-1	
			if kv < 100:
				kv_str = ("  " + str(kv))
			elif kv >= 100:
				kv_str = (" " + str(kv))	
			textokv.delete("1.0","end")
			textokv.insert(INSERT, (kv_str))
	
	def release_kv_cont_down(e):
		global releasekvdown
		releasekvdown = True
	#seleccion kilovoltios fluoro
	def click_kvf_cont_down():
		global kvf
		global kvf_str
		global releasekvfdown
		releasekvfdown = False
		while not releasekvfdown:
			time.sleep(0.2)

			if kvf== 40:
				kvf=kvf
			else:
				kvf=kvf-1	
			if kvf < 100:
				kvf_str = ("  " + str(kvf))
			elif kvf >= 100:
				kvf_str = (" " + str(kvf))	
			textokvf.delete("1.0","end")
			textokvf.insert(INSERT, (kvf_str))
	
	def release_kvf_cont_down(e):
		global releasekvfdown
		releasekvfdown = True

	def click_kvf_cont_up():
		global kvf
		global kvf_str
		global releasekvfup
		releasekvfup = False
		while not releasekvfup:
			time.sleep(0.2)

			if kvf==125:
				kvf=kvf
			else:
				kvf= kvf + 1
			if kvf < 100:
				kvf_str = ("  " + str(kvf))
			elif kvf >= 100:
				kvf_str = (" " + str(kvf))	
			textokvf.delete("1.0","end")
			textokvf.insert(INSERT, (kvf_str))


	def release_kvf_cont_up(e):
		global releasekvfup
		releasekvfup = True

	def click_shoot():
		global frequency
		global duration
		global releaseshoot
		global sg
		global contador_alarma
		global contador_servicio
		releaseshoot = False

		if not releaseshoot:
			

			shoot_s = Label(main_frame, image = simbolorx_on_s,  bg="grey")
			shoot_s.place(x=500, y= 515)
			frequency = 2000
			duration = int(sg*1000)
			winsound.Beep(frequency, duration)
			shoot_s = Label(main_frame, image = simbolorx_off_s,  bg="grey")
			shoot_s.place(x=500, y= 515)
			time.sleep(1)
			img = Image.open(img_db.image_db.torax_pa)
			img.show()
			contador_alarma = contador_alarma + 1
			if contador_alarma >= 8 :
				alarma_on()
			contador_temp = random.randint(1, 10)
		
			if contador_temp == 2:
				frequency = 2000
				duration = 1000000
				tube_temp_s = Label(main_frame, image = temperatura_on_s,  bg="grey")
				tube_temp_s.place(x=90, y= 515)
				time.sleep(1)
				alarma_on()
				time.sleep(3)

			else:
				frequency = 500

	def alarma_on():
		global duration
		global frequency
		global contador_servicio
		global duration
		ready_off_off_s = Label(main_frame, image = ready_off_s,  bg="grey")
		ready_off_off_s.place(x=425, y= 510)
		duration = int(1000000)
		alarm_s = Label(main_frame, image=alarm_on_s)
		alarm_s.place(x=225, y= 512)
		winsound.Beep(frequency, duration)

	def alarm_off():
		global duration
		global frequency
		global contador_alarma
		frequency = 500
		duration = int(0)
		ready_off_off_s = Label(main_frame, image = ready_on_s,  bg="grey")
		ready_off_off_s.place(x=425, y= 510)
		alarm_s = Label(main_frame, image=alarm_off_s)
		alarm_s.place(x=225, y= 512)	

		winsound.Beep(frequency, duration)
		contador_alarma = 0

	def temp_off():
		global duration
		global frequency
		global contador_alarma
		frequency = 500
		duration = int(0)
	
		tube_temp_s = Label(main_frame, image = temperatura_off_s,  bg="grey")
		tube_temp_s.place(x=90, y= 515)	
		winsound.Beep(frequency, duration)
		contador_alarma = 0


			

	def release_shoot(e):
		global releaseshoot
		time.sleep(0.1)
		releaseshoot = True
		shoot_s = Label(main_frame, image = simbolorx_off_s,  bg="grey")
		shoot_s.place(x=500, y= 515)




	def mAup():
		global mA
		global mA_str
		if mA == 10:
			mA = 16
		elif mA == 16:
			mA = 25
		elif mA == 25:
			mA = 50
		elif mA == 50:
			mA = 100
		elif mA == 100:
			mA = 160
		elif mA == 160:
			mA = 200
		elif mA == 200:
			mA = 250
		elif mA == 250:
			mA = 300
		elif mA == 300:
			mA = 400
		elif mA == 400:
			mA = 500
		elif mA == 500:
			mA = 600		
		mAs = mA * sg
		if mA < 100:
			mA_str = ("  " + str(mA))
		elif mA >= 100:
			mA_str = (" " + str(mA))
		textosg.delete("1.0","end")			
		textosg.insert(INSERT, round(sg , 2))
		textomAs.delete("1.0","end")
		textomAs.insert(INSERT, mAs )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA_str )
		

	def mAdown():
		global mA
		global mAs
		global mA_str
		if mA == 600:
			mA = 500
		elif mA == 500:
			mA = 400
		elif mA == 400:
			mA = 300
		elif mA == 300:
			mA = 250
		elif mA == 250:
			mA = 200
		elif mA == 200:
			mA = 160
		elif mA == 160:
			mA = 100
		elif mA == 100:
			mA = 50
		elif mA == 50:
			mA = 25
		elif mA == 25:
			mA=16
		elif mA == 16:
			mA=10
			
		mAs = mA * sg
		if mA < 100:
			mA_str = ("  " + str(mA))
		elif mA >= 100:
			mA_str = (" " + str(mA))
		textosg.delete("1.0","end")			
		textosg.insert(INSERT, round(sg , 2))
		textomAs.delete("1.0","end")
		textomAs.insert(INSERT, mAs )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA_str )

	def mAs_up_sel():
		global mAs
		global mA
		global mA_str	
		if sg >= 0.5:
			mAup()
			if 	mA == 10:
				mA == 16
			elif mA == 16:
				mA = 25
			elif mA == 25:
				mA = 50
			elif mA == 50:
				mA = 100
			elif mA == 100:
				mA = 160
			elif mA == 160:
				mA = 200
			elif mA == 200:
				mA = 250
			elif mA == 250:
				mA = 300
			elif mA == 300:
				mA = 400
			elif mA == 400:
				mA = 500
			elif mA == 500:
				mA = 600
		else:
			sgup()

		mAs = mA*sg
		textosg.delete("1.0","end")			
		textosg.insert(INSERT, round(sg , 2))
		textomAs.delete("1.0","end")
		textomAs.insert(INSERT, mAs )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA_str )
	



	def mAs_down_sel():
		global sg
		global mA
		global mAs
		global mA_str
		if sg >= 0.5:
			mAdown()
			if mA == 600:
				mA = 500
			elif mA == 500:
				mA = 400
			elif mA == 400:
				mA = 300
			elif mA == 300:
				mA = 250
			elif mA == 250:
				mA = 200
			elif mA == 200:
				mA = 160
			elif mA == 160:
				mA = 100
			elif mA == 100:
				mA = 50
			elif mA == 50:
				mA = 25
			elif mA == 25:
				mA=16
			elif mA == 16:
				mA=10
		if mA == 10 and sg <= 1:
			sgdown()
		
		mAs = mA*sg
		textosg.delete("1.0","end")			
		textosg.insert(INSERT, round(sg , 2))
		textomAs.delete("1.0","end")
		textomAs.insert(INSERT, mAs )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA_str )



	def sgup():
		global sg
		global mA_str
		sg= sg + 0.05

		if sg >= 5.0:
			sg = 5.0
		mAs = mA*sg	
		textosg.delete("1.0","end")			
		textosg.insert(INSERT, round(sg , 2))
		textomAs.delete("1.0","end")
		textomAs.insert(INSERT, mAs )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA_str )

	def sgdown():
		global sg
		global mA_str
		sg= sg - 0.05
		if sg <= 0.05:
			sg = 0.05	
		round(sg ,2)
		mAs = mA*sg
		textosg.delete("0.1","end")				
		textosg.insert(INSERT, round(sg , 2))
		textomAs.delete("1.0","end")
		textomAs.insert(INSERT, mAs )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA_str )

	def b_mesa_pressed():
		boton_b_mesa = Button(root , width = 50, height = 50, image = b_mesa_yellow_s, command = b_mesa_pressed)
		boton_b_mesa.place(x=450 , y = 600)
		boton_b_mural = Button(root,  width = 50, height = 50, image = b_mural_s,   command = b_mural_pressed)
		boton_b_mural.place(x=450, y = 670)
		boton_directo = Button(root,  width = 50, height = 50,image = directo_s,   command = directo_pressed)
		boton_directo.place(x=600, y = 670)

	def b_mural_pressed():
		boton_b_mesa = Button(root , width = 50, height = 50, image = b_mesa_s, command = b_mesa_pressed)
		boton_b_mesa.place(x=450 , y = 600)
		boton_b_mural = Button(root,  width = 50, height = 50, image = b_mural_yellow_s,   command = b_mural_pressed)
		boton_b_mural.place(x=450, y = 670)
		boton_directo = Button(root,  width = 50, height = 50,image = directo_s, command = directo_pressed)
		boton_directo.place(x=600, y = 670)

	def directo_pressed():
		boton_b_mesa = Button(root , width = 50, height = 50, image = b_mesa_s, command = b_mesa_pressed)
		boton_b_mesa.place(x=450 , y = 600)
		boton_b_mural = Button(root,  width = 50, height = 50, image = b_mural_s, command = b_mural_pressed)
		boton_b_mural.place(x=450, y = 670)
		boton_directo = Button(root,  width = 50, height = 50,image = directo_yellow_s,   command = directo_pressed)
		boton_directo.place(x=600, y = 670)

	def cam1_pressed():
		boton_cam1 = Button(root, image = imagen_cam1_yellow_s , width = 50, height = 50,  command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)

	def cam2_pressed():
		boton_cam2 = Button(root, image = imagen_cam2_yellow_s , width = 50, height = 50,  command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
			
	def cam3_pressed():
		boton_cam3 = Button(root, image = imagen_cam3_yellow_s , width = 50, height = 50,  command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)

	def reset():
		
		mAlabel = Label(root, text= 'mAs', font=("Consolas",25), bg="black", fg = "red")
		mAlabel.place(x=850, y= 230)
	def sens_s_up():
		global sens_s_s
		global sens_s_s_str		
		if sens_s_s <=4:
			sens_s_s  = sens_s_s + 1
		if sens_s_s > -1:
			sens_s_s_str = (" " + str(sens_s_s))
		else:
			sens_s_s_str = ("" + str(sens_s_s))
		texto_sens.delete("1.0","end")
		texto_sens.insert(INSERT, sens_s_s_str )

	def sens_s_down():
		global sens_s_s
		global sens_s_s_str
		if sens_s_s >=-4:
			sens_s_s  = sens_s_s - 1
			sens_s_s_str = ("" + str(sens_s_s))

		texto_sens.delete("1.0","end")
		texto_sens.insert(INSERT, sens_s_s_str )


	def mA_f_up():
		global mA_f
		
		if mA_f < 5:
			mA_f  = mA_f + 0.1
		texto_ma_f.delete("1.0","end")
		texto_ma_f.insert(INSERT, mA_f )

	def mA_f_auto():
		global mA_f
		mA_f = 0.1

		texto_ma_f.delete("1.0","end")
		texto_ma_f.insert(INSERT, mA_f )






	root = Toplevel(borderwidth= 50, relief = "flat")

	ancho_ventana = 1425
	alto_ventana = 950
	main_frame = Frame (root, bg = "grey")
	main_frame.config(width=1220, height=600)
	main_frame.pack(side = BOTTOM, pady = 10)	
	top_frame = Frame (root, bg = "grey")
	top_frame.config(width=1220, height=180)
	top_frame.pack(side = TOP, pady = 10)
	x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
	y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

	posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana-90)
	root.geometry(posicion)

	root.resizable(0,0)
	root.title("                                                                                                                         SIMULADOR CONSOLA MPS 64RF SEDECAL REALIZADO POR XRAY SERVICE SOLUTIONS")
	root.iconbitmap(f'{cwd}/xray.ico')


	imagen_cam1_s = PhotoImage(file=f'{cwd}/cam_1.png')
	imagen_cam2_s = PhotoImage(file=f'{cwd}/cam_2.png')
	imagen_cam3_s = PhotoImage(file=f'{cwd}/cam_3.png')
	imagen_cam1_yellow_s = PhotoImage(file=f'{cwd}/cam1yellow.png')
	imagen_cam2_yellow_s = PhotoImage(file=f'{cwd}/cam2yellow.png')
	imagen_cam3_yellow_s = PhotoImage(file=f'{cwd}/cam3yellow.png')
	imagen_sens1_s = PhotoImage(file=f'{cwd}/sens1.png')
	imagen_sens2_s = PhotoImage(file=f'{cwd}/sens2.png')
	imagen_sens3_s = PhotoImage(file=f'{cwd}/sens3.png')
	imagen_sens1_yellow_s = PhotoImage(file=f'{cwd}/sens1_yellow.png')
	imagen_sens2_yellow_s = PhotoImage(file=f'{cwd}/sens2_yellow.png')
	imagen_sens3_yellow_s = PhotoImage(file=f'{cwd}/sens3_yellow.png')

	imagen_smallman_s = PhotoImage(file=f'{cwd}/smallman.png')
	imagen_bigman_s = PhotoImage(file=f'{cwd}/bigman.png')
	b_mesa_s = PhotoImage(file=f'{cwd}/b_mesa.png')
	b_mural_s = PhotoImage(file=f'{cwd}/b_mural.png')
	directo_s = PhotoImage(file=f'{cwd}/directo_s.png')
	b_mesa_yellow_s = PhotoImage(file=f'{cwd}/b_mesa_yellow.png')
	b_mural_yellow_s = PhotoImage(file=f'{cwd}/b_mural_yellow.png')
	directo_yellow_s = PhotoImage(file=f'{cwd}/directo_on_s.png')
	on_s = PhotoImage(file=f'{cwd}/on_button_s.png')
	off_s = PhotoImage(file=f'{cwd}/off_button_s.png')
	disparo_s = PhotoImage(file=f'{cwd}/shoot_s.png')
	black_s = PhotoImage(file=f'{cwd}/black.png')
	ff_s = PhotoImage(file=f'{cwd}/ff_spot_s.png')
	fg_s = PhotoImage(file=f'{cwd}/fg_spot_S.png')
	alarm_off_s = PhotoImage(file=f'{cwd}/alarm_off_s.png')
	alarm_on_s = PhotoImage(file=f'{cwd}/alarm_on_s.png')
	up_button_s = PhotoImage(file=f'{cwd}/up_button_s.png')
	down_button_s = PhotoImage(file=f'{cwd}/down_button_s.png')
	sense_s_s = PhotoImage(file=f'{cwd}/sense_s_s.png')
	sense_m_s = PhotoImage(file=f'{cwd}/sense_m_s.png')
	sense_f_s = PhotoImage(file=f'{cwd}/sense_f_s.png')
	directo_s_s = PhotoImage(file=f'{cwd}/directo_s.png')
	bucky_mesa_s = PhotoImage(file=f'{cwd}/b_mesa_s.png')
	bucky_mural_s = PhotoImage(file=f'{cwd}/b_mural_s.png')
	tomo_s = PhotoImage(file=f'{cwd}/tomo_s.png')
	direct_remote_s = PhotoImage(file=f'{cwd}/direct_remote_s.png')
	bucky_remote_s = PhotoImage(file=f'{cwd}/bucky_remote_s.png')
	ii_remote_s = PhotoImage(file=f'{cwd}/ii_remote_s.png')
	tomo_remote_s = PhotoImage(file=f'{cwd}/tomo_remote_s.png')
	reset_s = PhotoImage(file=f'{cwd}/reset_s.png')
	contraste_s = PhotoImage(file=f'{cwd}/contraste_s.png')
	fluoro_auto_s = PhotoImage(file=f'{cwd}/fluoro_auto_s.png')
	ii_mag1_s = PhotoImage(file=f'{cwd}/ii_1_s.png')
	ii_mag2_s = PhotoImage(file=f'{cwd}/ii_2_s.png')
	ii_mag3_s = PhotoImage(file=f'{cwd}/ii_3_s.png')
	fluoro_pulsed_s = PhotoImage(file=f'{cwd}/fluoro_pulsed_s.png')
	fluoro_1_s = PhotoImage(file=f'{cwd}/fluoro_1_s.png')
	ready_on_s = PhotoImage(file=f'{cwd}/ready_on_s.png')
	ready_off_s = PhotoImage(file=f'{cwd}/ready_off_s.png')
	temperatura_on_s = PhotoImage(file=f'{cwd}/tube_temp_on_s.png')
	temperatura_off_s = PhotoImage(file=f'{cwd}/tube_temp_off_s.png')
	blanking_s = PhotoImage(file=f'{cwd}/blanking_s.png')
	pulsed_label_s = PhotoImage(file=f'{cwd}/fluoro_pulsed_label_s.png')
	child_s = PhotoImage(file=f'{cwd}/child_s.png')
	woman_s = PhotoImage(file=f'{cwd}/woman_s.png')
	small_man_s = PhotoImage(file=f'{cwd}/small_man_s.png')
	big_man_s = PhotoImage(file=f'{cwd}/big_man_s.png')
	tubo_s = PhotoImage(file=f'{cwd}/tubo_s.png')	
	puesto_s = PhotoImage(file=f'{cwd}/puesto_s.png')
	apr_1_s = PhotoImage(file=f'{cwd}/apr_1_s.png')
	apr_2_s = PhotoImage(file=f'{cwd}/apr_2_s.png')
	apr_3_s = PhotoImage(file=f'{cwd}/apr_3_s.png')
	apr_4_s = PhotoImage(file=f'{cwd}/apr_4_s.png')
	apr_5_s = PhotoImage(file=f'{cwd}/apr_5_s.png')
	apr_6_s = PhotoImage(file=f'{cwd}/apr_6_s.png')
	apr_7_s = PhotoImage(file=f'{cwd}/apr_7_s.png')
	apr_8_s = PhotoImage(file=f'{cwd}/apr_8_s.png')
	prep_s = PhotoImage(file=f'{cwd}/prep_s.png')




	simbolorx_off_s = PhotoImage(file=f'{cwd}/simbolorx_off_s.png')
	simbolorx_on_s = PhotoImage(file=f'{cwd}/simbolorx_on_s.png')
	boton_shoot = Button(root , image = disparo_s , width = 40, height = 40, bg="green")
	boton_shoot.place(x=1125 , y = 845)
	boton_shoot.bind('<Button-1>', lambda e: Thread(target=click_shoot, daemon=True).start())
	boton_shoot.bind('<ButtonRelease-1>', release_shoot)
	boton_prep = Button(root , image = prep_s , width = 40, height = 40, bg="grey" , command = temp_off)
	boton_prep.place(x=1025 , y = 845)
	foco_fino_label = Label(main_frame, image = ff_s, width=40	, height=40,  bg="grey", fg = "black")
	foco_fino_label.place(x=520, y= 80)
	foco_grueso_label = Label(main_frame, image = fg_s, width=40	, height=40,  bg="grey", fg = "black")
	foco_grueso_label.place(x=520, y= 150)



	alarm_display_label = Label(main_frame, image=black_s)
	alarm_display_label.place(x=1300 , y =120)
	ready_label = Label(main_frame, image=ready_off_s, bg="black")
	ready_label.place(x=1330 , y =120)

	textokv = Text(main_frame)	
	textokv.config( width=4, height=1,  font=("Consolas",30), bg="black", fg ="light green") 
	textokv.insert(INSERT, (kv_str))
	textokv.place(x=70 , y = 250) 
	kvlabel = Label(main_frame, text="Kvp", font=("Consolas", 15, "bold"), bg="grey" , fg = "black")
	kvlabel.place(x=95, y= 310)
	
	boton_subirkv = Button(main_frame, image = up_button_s, width = 40, height = 40,bg ="white", font=("Consolas",20))
	boton_subirkv.place(x=92, y = 340)
	boton_subirkv.bind('<Button-1>', lambda e: Thread(target=click_kv_cont_up, daemon=True).start())
	boton_subirkv.bind('<ButtonRelease-1>', release_kv_cont_up)
	boton_bajarkv = Button(main_frame, image = down_button_s , width = 40, height = 40,bg ="white", font=("Consolas",20))
	boton_bajarkv.place(x=92 , y = 415)
	boton_bajarkv.bind('<Button-1>', lambda e: Thread(target=click_kv_cont_down, daemon=True).start())
	boton_bajarkv.bind('<ButtonRelease-1>', release_kv_cont_down)


	textomAs = Text(main_frame)
	textomAs.config( width=4, height=1, font=("Consolas",30), bg="black", fg = "light green") 
	textomAs.insert(INSERT, (mAs))
	textomAs.place(x=205 , y = 250) 
	mAslabel = Label(main_frame, text='mAs', font=("Consolas",15, "bold"), bg="grey", fg = "black")
	mAslabel.place(x=230, y= 310)
	boton_subirmAs = Button(main_frame, image = up_button_s, width = 40, height = 40,bg ="white", font=("Consolas",20),  command = mAs_up_sel)
	boton_subirmAs.place(x=227, y = 340)
	boton_bajarmAs = Button(main_frame, image = down_button_s, width =40, height = 40,bg ="white", font=("Consolas",20), command = mAs_down_sel)
	boton_bajarmAs.place(x=227 , y = 415)

	textomA = Text(main_frame)
	textomA.config( width=4, height=1, font=("Consolas",30), bg="black", fg = "light green") 
	textomA.insert(INSERT, (mA_str))
	textomA.place(x=340 , y = 250) 
	mAlabel = Label(main_frame, text='mA', font=("Consolas",15, "bold"), bg="grey", fg = "black")
	mAlabel.place(x=370, y= 310)
	boton_subirmA = Button(main_frame, image = up_button_s, width = 40, height = 40,bg ="white", font=("Consolas",20),  command = mAup)
	boton_subirmA.place(x=362, y = 340)
	boton_bajarmA = Button(main_frame, image = down_button_s, width =40, height = 40,bg ="white", font=("Consolas",20), command = mAdown)
	boton_bajarmA.place(x=362 , y = 415)


	textosg = Text(main_frame)
	textosg.config( width=4, height=1, font=("Consolas",30), bg="black", fg = "light green") 
	textosg.insert(INSERT, sg )
	textosg.place(x=475 , y = 250) 
	sglabel = Label(main_frame, text="s", font=("Consolas", 15, "bold"), bg="grey", fg = "black")
	sglabel.place(x=510, y= 310)
	boton_subirsg = Button(main_frame, image = up_button_s, width =40, height = 40,bg ="white", font=("Consolas",20),  command = sgup)
	boton_subirsg.place(x=497, y = 340)
	boton_bajarsg = Button(main_frame,image = down_button_s, width = 40, height = 40,bg ="white", font=("Consolas",20), command = sgdown)
	boton_bajarsg.place(x=497 , y = 415)


	boton_subir_sens = Button(main_frame, image = up_button_s, width =40, height = 40,bg ="white", font=("Consolas",20),  command = sens_s_up)
	boton_subir_sens.place(x=750, y = 340)
	boton_bajar_sens = Button(main_frame,image = down_button_s, width = 40, height = 40,bg ="white", font=("Consolas",20), command = sens_s_down)
	boton_bajar_sens.place(x=750 , y = 415)
	texto_sens = Text(main_frame)
	texto_sens.config( width=3, height=1, font=("Consolas",30), bg="black", fg = "light green") 
	texto_sens.insert(INSERT, sens_s_s_str )
	texto_sens.place(x=735 , y = 250) 
	sens_label_s = Label(main_frame, image = blanking_s,  bg="grey")
	sens_label_s.place(x=760, y= 310)

	boton_cam1 = Button(main_frame, image = imagen_cam1_s , width = 40, height = 40, command = cam1_pressed)
	boton_cam1.place(x=680 , y = 150)
	boton_cam2 = Button(main_frame, image = imagen_cam2_s , width = 40, height = 40, command = cam2_pressed)
	boton_cam2.place(x=750 , y = 150)
	boton_cam3 = Button(main_frame, image = imagen_cam3_s , width = 40, height = 40, command = cam3_pressed)
	boton_cam3.place(x=820 , y = 150)


	boton_sens1 = Button(main_frame, image = sense_s_s , width = 40, height = 40, command = None)
	boton_sens1.place(x=680 , y = 80)
	boton_sens2 = Button(main_frame, image = sense_m_s , width = 40, height = 40, command = None)
	boton_sens2.place(x=750 , y = 80)
	boton_sens3 = Button(main_frame, image = sense_f_s , width = 40, height = 40, command = None)
	boton_sens3.place(x=820 , y = 80)


	boton_reset = Button(main_frame, image = reset_s , width = 40, height = 40, bg ="white", command = alarm_off)
	boton_reset.place(x=750 , y = 505)

	boton_ii_1_s = Button(main_frame, image = ii_mag1_s , width = 40, height = 40, command = None)
	boton_ii_1_s.place(x=970 , y = 80)
	boton_ii_2_s = Button(main_frame, image = ii_mag2_s , width = 40, height = 40, command = None)
	boton_ii_2_s.place(x=1040 , y = 80)
	boton_ii_3_s = Button(main_frame, image = ii_mag3_s , width = 40, height = 40, command = None)
	boton_ii_3_s.place(x=1110 , y = 80)
	fluoro1_s = Button(main_frame, image = fluoro_1_s , width = 40, height = 40, command = None)
	fluoro1_s.place(x=1110 , y = 150)
	min_f = Text(main_frame)
	min_f.config( width=1, height=1, font=("Consolas",30), bg="black", fg = "light green") 
	min_f.insert(INSERT, t_f )
	min_f.place(x=980 , y = 150) 
	min_f_label = Label(main_frame, text="min", font=("Consolas", 15, "bold"), bg="grey", fg = "black")
	min_f_label.place(x=975, y= 205)

	textokvf = Text(main_frame)	
	textokvf.config( width=4, height=1,  font=("Consolas",30), bg="black", fg ="light green") 
	textokvf.insert(INSERT, kvf_str)
	textokvf.place(x=1085 , y = 250) 
	kvlabelf = Label(main_frame, text="Kvp", font=("Consolas", 15, "bold"), bg="grey" , fg = "black")
	kvlabelf.place(x=1115, y= 310)
	boton_subir_kvp_f_s = Button(main_frame, image = up_button_s, width = 40, height = 40,bg ="white", font=("Consolas",20))
	boton_subir_kvp_f_s.place(x=1110, y = 340)
	boton_subir_kvp_f_s.bind('<Button-1>', lambda e: Thread(target=click_kvf_cont_up, daemon=True).start())
	boton_subir_kvp_f_s.bind('<ButtonRelease-1>', release_kvf_cont_up)
	boton_bajar_kvp_f_s = Button(main_frame, image = down_button_s , width = 40, height = 40,bg ="white", font=("Consolas",20))
	boton_bajar_kvp_f_s.place(x=1110 , y = 415)
	boton_bajar_kvp_f_s.bind('<Button-1>', lambda e: Thread(target=click_kvf_cont_down, daemon=True).start())
	boton_bajar_kvp_f_s.bind('<ButtonRelease-1>', release_kvf_cont_down)
	boton_contraste_s = Button(main_frame, image = contraste_s, width =40, height = 40,bg ="white", font=("Consolas",20),  command = mA_f_up)
	boton_contraste_s.place(x=970, y = 340)
	texto_ma_f = Text(main_frame)
	texto_ma_f.config( width=3, height=1, font=("Consolas",30), bg="black", fg = "light green") 
	texto_ma_f.insert(INSERT, mA_f )
	texto_ma_f.place(x=955 , y = 250) 
	ma_f_label = Label(main_frame, text="mA", font=("Consolas", 15, "bold"), bg="grey", fg = "black")
	ma_f_label.place(x=975, y= 310)
	boton_abc_f_s = Button(main_frame,image = fluoro_auto_s, width = 40, height = 40,bg ="white", font=("Consolas",20), command = mA_f_auto	)
	boton_abc_f_s.place(x=970 , y = 415)
	boton_pulsed_f_s = Button(main_frame, image = fluoro_pulsed_s , width = 40, height = 40, command = alarm_off)
	boton_pulsed_f_s.place(x=1110 , y = 505)
	pulses_f_s = Text(main_frame)
	pulses_f_s.config( width=3, height=1, font=("Consolas",30), bg="black", fg = "light green") 
	pulses_f_s.insert(INSERT, p_f_s )
	pulses_f_s.place(x=955 , y = 503) 	


	boton_directo = Button(main_frame,  width = 40, height = 40,image = directo_s, bg ="white",   command = None)
	boton_directo.place(x=190, y = 80)
	boton_mesa = Button(main_frame,  width = 40, height = 40,image = bucky_mesa_s, bg ="white",   command = None)
	boton_mesa.place(x=260, y = 80)
	boton_mural= Button(main_frame,  width = 40, height = 40,image = bucky_mural_s, bg ="white",   command = None)
	boton_mural.place(x=330, y = 80)
	boton_tomo = Button(main_frame,  width = 40, height = 40,image = tomo_s, bg ="white",   command = None)
	boton_tomo.place(x=400, y = 80)

	boton_telemando2_1 = Button(main_frame,  width = 40, height = 40, image = direct_remote_s, bg ="white",   command = None)
	boton_telemando2_1.place(x=190, y = 150)
	boton_telemando2_2 = Button(main_frame,  width = 40, height = 40,image = bucky_remote_s, bg ="white",   command = None)
	boton_telemando2_2.place(x=260, y = 150)
	boton_telemando2_3 = Button(main_frame,  width = 40, height = 40, image = ii_remote_s, bg ="white",   command = None)
	boton_telemando2_3.place(x=330, y = 150)
	boton_telemando2_4 = Button(main_frame,  width = 40, height = 40, image = tomo_remote_s, bg ="white",   command = None)
	boton_telemando2_4.place(x=400, y = 150)
	
	boton_on = Button(main_frame , width = 40, height = 40, image = on_s, command = None)
	boton_on.place(x=70 , y = 80)
	boton_off = Button(main_frame , width = 40, height = 40, image = off_s, command = None)
	boton_off.place(x=70 , y = 150)
	tube_temp_s = Label(main_frame, image = temperatura_off_s,  bg="grey")
	tube_temp_s.place(x=90, y= 515)
	alarm_s = Label(main_frame, image = alarm_off_s,  bg="grey")
	alarm_s.place(x=225, y= 512)
	ready_on_on_s = Label(main_frame, image = ready_on_s,  bg="grey")
	ready_on_on_s.place(x=425, y= 510)
	shoot_s = Label(main_frame, image = simbolorx_off_s,  bg="grey")
	shoot_s.place(x=500, y= 515)
	pulsada_label_s = Label(main_frame, image = pulsed_label_s,  bg="grey")
	pulsada_label_s.place(x=1045, y= 505)

	boton_child_s = Button(top_frame, image = child_s , width = 40, height = 40, command = None)
	boton_child_s.place(x=900 , y = 65)
	boton_woman_s = Button(top_frame, image = woman_s , width = 40, height = 40, command = None)
	boton_woman_s.place(x=970 , y = 65)
	boton_small_man_s = Button(top_frame, image = small_man_s , width = 40, height = 40, command = None)
	boton_small_man_s.place(x=1040 , y = 65)
	boton_big_man_s = Button(top_frame, image = big_man_s , width = 40, height = 40, command = None)
	boton_big_man_s.place(x=1110 , y = 65)
	boton_tubo_s = Button(top_frame, image = tubo_s , width = 40, height = 40, command = None)
	boton_tubo_s.place(x=800 , y =30)
	boton_puesto_s = Button(top_frame, image = puesto_s , width = 40, height = 40, command = None)
	boton_puesto_s.place(x =800 , y = 100)
	boton_1_s = Button(top_frame, image = apr_1_s , width = 40, height = 40, command = None)
	boton_1_s.place(x=500, y =30)
	boton_2_s = Button(top_frame, image = apr_2_s , width = 40, height = 40, command = None)
	boton_2_s.place(x =570 , y = 30)
	boton_3_s = Button(top_frame, image = apr_3_s , width = 40, height = 40, command = None)
	boton_3_s.place(x=640 , y =30)
	boton_4_s = Button(top_frame, image = apr_4_s , width = 40, height = 40, command = None)
	boton_4_s.place(x =710 , y = 30)
	boton_5_s = Button(top_frame, image = apr_5_s , width = 40, height = 40, command = None)
	boton_5_s.place(x=500 , y = 100)
	boton_6_s = Button(top_frame, image = apr_6_s , width = 40, height = 40, command = None)
	boton_6_s.place(x =570 , y = 100)
	boton_7_s = Button(top_frame, image = apr_7_s , width = 40, height = 40, command = None)
	boton_7_s.place(x=640 , y = 100)
	boton_8_s = Button(top_frame, image = apr_8_s , width = 40, height = 40, command = None)
	boton_8_s.place(x =710 , y = 100)

	apr_name_1 = Text(top_frame)	
	apr_name_1.config( width=8, height=1,  font=("Consolas",15), bg="black", fg ="light green") 
	apr_name_1.insert(INSERT, text_1)
	apr_name_1.place(x=50 , y = 60) 
	apr_name_1 = Label(top_frame, text="1", font=("Consolas", 15, "bold"), bg="grey" , fg = "black")
	apr_name_1.place(x=85, y= 30)
	apr_name_2 = Text(top_frame)	
	apr_name_2.config( width=8, height=1,  font=("Consolas",15), bg="black", fg ="light green") 
	apr_name_2.insert(INSERT, text_2)
	apr_name_2.place(x=140 , y = 60) 
	apr_name_2 = Label(top_frame, text="2", font=("Consolas", 15, "bold"), bg="grey" , fg = "black")
	apr_name_2.place(x=175, y= 30)
	apr_name_3 = Text(top_frame)	
	apr_name_3.config( width=8, height=1,  font=("Consolas",15), bg="black", fg ="light green") 
	apr_name_3.insert(INSERT, text_3)
	apr_name_3.place(x=230 , y = 60) 
	apr_name_3 = Label(top_frame, text="3", font=("Consolas", 15, "bold"), bg="grey" , fg = "black")
	apr_name_3.place(x=265, y= 30)
	apr_name_4 = Text(top_frame)	
	apr_name_4.config( width=8, height=1,  font=("Consolas",15), bg="black", fg ="light green") 
	apr_name_4.insert(INSERT, text_4)
	apr_name_4.place(x=320 , y = 60) 
	apr_name_4 = Label(top_frame, text="4", font=("Consolas", 15, "bold"), bg="grey" , fg = "black")
	apr_name_4.place(x=355, y= 30)
	apr_name_5 = Text(top_frame)	
	apr_name_5.config( width=8, height=1,  font=("Consolas",15), bg="black", fg ="light green") 
	apr_name_5.insert(INSERT, text_5)
	apr_name_5.place(x=50 , y = 85) 
	apr_name_5 = Label(top_frame, text="5", font=("Consolas", 15, "bold"), bg="grey" , fg = "black")
	apr_name_5.place(x=85, y= 115)
	apr_name_6 = Text(top_frame)	
	apr_name_6.config( width=8, height=1,  font=("Consolas",15), bg="black", fg ="light green") 
	apr_name_6.insert(INSERT, text_6)
	apr_name_6.place(x=140 , y = 85) 
	apr_name_6 = Label(top_frame, text="6", font=("Consolas", 15, "bold"), bg="grey" , fg = "black")
	apr_name_6.place(x=175, y= 115)
	apr_name_7 = Text(top_frame)	
	apr_name_7.config( width=8, height=1,  font=("Consolas",15), bg="black", fg ="light green") 
	apr_name_7.insert(INSERT, text_7)
	apr_name_7.place(x=230 , y = 85) 
	apr_name_7 = Label(top_frame, text="7", font=("Consolas", 15, "bold"), bg="grey" , fg = "black")
	apr_name_7.place(x=265, y= 115)
	apr_name_8 = Text(top_frame)	
	apr_name_8.config( width=8, height=1,  font=("Consolas",15), bg="black", fg ="light green") 
	apr_name_8.insert(INSERT, text_8)
	apr_name_8.place(x=320 , y = 85) 
	apr_name_8 = Label(top_frame, text="8", font=("Consolas", 15, "bold"), bg="grey" , fg = "black")
	apr_name_8.place(x=355, y= 115)





	root.mainloop()


sedecal()

