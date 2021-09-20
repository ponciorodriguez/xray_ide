from tkinter import *
from threading import Thread
import time
import winsound
import random
import os
cwd = os.path.dirname(__file__)


kv = int()
kv = 40
mA = int()
mA = 10
sg = float()
sg = 0.10
fs = float()
fs = 40
ct = int()
ct = 0
cm = int()
cm = 0
puntos = str()
puntos = 'mA'
sin_seg = str()
sin_seg = 'sg'
miliseg = float()
mas_sel = 0
mAs_calc = float()
mAs = float()
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









def philips():
	def click_kv_cont_down():
		global kv
		global releasekvdown
		releasekvdown = False
		while not releasekvdown:
			time.sleep(0.3)
			textokv.delete("1.0","end")
			if kv== 40:
				kv=kv
			else:
				kv=kv-1	
			textokv.insert(INSERT, kv )
		
	def release_kv_cont_down(e):
		global releasekvdown
		releasekvdown = True

	def click_kv_cont_up():
		global kv
		global releasekvup
		releasekvup = False
		while not releasekvup:
			time.sleep(0.3)
			textokv.delete("1.0","end")
			if kv==150:
				kv=kv
			else:
				kv= kv + 1
			textokv.insert(INSERT, kv )


	def release_kv_cont_up(e):
		global releasekvup
		releasekvup = True

	def click_shoot():
		global frequency
		global duration
		global releaseshoot
		global sg
		global contador_alarma
		global contador_servicio
		releaseshoot = False

		if not releaseshoot:
			

			rxon=Label(root, image=imagen_shoot, bg="black")
			rxon.place(x=400 , y =120) 
			frequency = 2000
			duration = int(sg*1000)
			winsound.Beep(frequency, duration)
			rxon=Label(root, image=black, bg ="black")
			rxon.place(x=400 , y =120) 
			contador_alarma = contador_alarma + 1
			if contador_alarma >= 8 :
				alarma_on()
			contador_servicio = random.randint(1, 10)
		
			if contador_servicio == 2:
				frequency = 3000
				duration = 1000000
				telefono_label = Label(root, image=telefono, bg="black")
				telefono_label.place(x=250 , y =120)
				time.sleep(1)
				alarma_on()
			else:
				frequency = 800

	def alarma_on():
		global duration
		global frequency
		global contador_servicio
		global duration
		ready_label = Label(root, image=black, bg="black")
		ready_label.place(x=350 , y =120)
		

		duration = int(1000000)
		alarm_display_label = Label(root, image=alarm_display)
		alarm_display_label.place(x=300 , y =120)
		winsound.Beep(frequency, duration)

	def alarm_off():
		global duration
		global frequency
		global contador_alarma
		ready_label = Label(root, image=ready, bg="black")
		ready_label.place(x=350 , y =120)
		frequency = 800
		duration = int(0)
		alarm_display_label = Label(root, image=black)
		alarm_display_label.place(x=300 , y =120)
		winsound.Beep(frequency, duration)
		telefono_label = Label(root, image=black, bg="black")
		telefono_label.place(x=250 , y =120)
		contador_alarma = 0



			

	def release_shoot(e):
		global releaseshoot
		time.sleep(0.1)
		releaseshoot = True
		rxon=Label(root, image=black, width=30	, height=30)
		rxon.place(x=400 , y =120) 

	def kv_mAs():
		global mas_sel
		global puntos
		global sg
		global miliseg
		global mA
		miliseg =mA*sg
		textomA.delete("1.0","end")
		textomA.insert(INSERT, miliseg )	
		mas_sel = 1
		mAlabel = Label(root, text= 'mAs', font=("Consolas",25), bg="black", fg = "red")
		mAlabel.place(x=850, y= 230)
		puntos = 'mA'
		mAlabel = Label(root, text=puntos, font=("Consolas",25), bg="black", fg = "red")
		mAlabel.place(x=850, y= 230)
		textosg.config( width=5, height=1, font=("Consolas",25), bg="black", fg = "black") 
		textosg.insert(INSERT, sg)
		textosg.place(x=935 , y = 220) 
		sglabel = Label(root, text='  ', font=("Consolas",25), bg="black", fg = "red")
		sglabel.place(x=1055, y= 230)
		boton_kv_mas = Button(root, text = "kV-mAs" , width = 11, height = 3, font=("Consolas",10),bg ="yellow", command = kv_mAs)
		boton_kv_mas.place(x=10 , y = 260)
		boton_kv_mas_s = Button(root, text = "kV-mA-s" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mA_sg)
		boton_kv_mas_s.place(x=110 , y = 260)
	def kv_mA_sg():
		global mas_sel
		global puntos
		global sg
		global mA
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		mas_sel = 0
		puntos = '    '
		mAlabel = Label(root, text= puntos, font=("Consolas",25), bg="black", fg = "red")
		mAlabel.place(x=850, y= 230)
		puntos = 'mA'
		mAlabel = Label(root, text='mA', font=("Consolas",25), bg="black", fg = "red")
		mAlabel.place(x=850, y= 230)
		textosg.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "red") 
		textosg.insert(INSERT, sg)
		textosg.place(x=935 , y = 220) 
		sglabel = Label(root, text='sg', font=("Consolas",25), bg="black", fg = "red")
		sglabel.place(x=1055, y= 230)
		boton_kv_mas = Button(root, text = "kV-mAs" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mAs)
		boton_kv_mas.place(x=10 , y = 260)
		boton_kv_mas_s = Button(root, text = "kV-mA-s" , width = 11, height = 3, font=("Consolas",10),bg ="yellow", command = kv_mA_sg)
		boton_kv_mas_s.place(x=110 , y = 260)



	def mAup():
		global mA
		global ct
		global mas_sel
		if mas_sel == 0:

			mA = 10
			if ct == 0:
				mA = 16
			elif ct == 1:
				mA = 25
			elif ct == 2:
				mA = 50
			elif ct == 3:
				mA = 100
			elif ct == 4:
				mA = 160
			elif ct == 5:
				mA = 200
			elif ct == 6:
				mA = 250
			elif ct == 7:
				mA = 300
			elif ct == 8:
				mA = 350
			elif ct == 9:
				mA = 400
			elif ct == 10:
				mA = 500		
			ct = ct +1
			if ct >=11:
				ct=0
				mA=mA
			textomA.delete("1.0","end")
			textomA.insert(INSERT, mA )
		else:
			mAs_up_sel()		

	def mAdown():
		
		global mA
		global mas_sel
		if mas_sel == 0:
		
			if mA == 500:
				mA = 400
			elif mA == 400:
				mA = 350
			elif mA == 350:
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
			textomA.delete("1.0","end")
			textomA.insert(INSERT, mA )	

		else:

			mAs_down_sel()

	def mAs_up_sel():
		global cm
		global mAs
		global miliseg
		global sg
		global mA	

		if cm == 0:
			miliseg = mA*sg
		elif cm == 1:
			miliseg = 25*0.1
		elif cm == 2:
			miliseg = 50*0.1
		elif cm == 3:
			miliseg = 100*0.1
		elif cm == 4:
			miliseg = 160*0.1
		elif cm == 5:
			miliseg = 200*0.1
		elif cm == 6:
			miliseg = 250*0.1
		elif cm == 7:
			miliseg = 300*0.1
		elif cm == 8:
			miliseg = 350*0.1
		elif cm == 9:
			miliseg = 400*0.1
		elif cm == 10:
			miliseg = 500*0.1		
		cm = cm +1
		if cm >=11:
			cm=0
		
		textomA.delete("1.0","end")
		textomA.insert(INSERT, miliseg )

	def mAs_down_sel():
		
		global cm
		global mAs
		global miliseg
		global sg
		global mA	

		if cm == 0:
			miliseg = mA*sg
		elif cm == 1:
			miliseg = 500*0.1
		elif cm == 2:
			miliseg = 400*0.1
		elif cm == 3:
			miliseg = 350*0.1
		elif cm == 4:
			miliseg = 300*0.1
		elif cm == 5:
			miliseg = 250*0.1
		elif cm == 6:
			miliseg = 200*0.1
		elif cm == 7:
			miliseg = 160*0.1
		elif cm == 8:
			miliseg = 100*0.1
		elif cm == 9:
			miliseg = 50*0.1
		elif cm == 10:
			miliseg = 25*0.1		
		cm = cm +1
		if cm >=11:
			cm=0
		
		textomA.delete("1.0","end")
		textomA.insert(INSERT, miliseg )

	# def mAs_down():
	# 	global mas_sel
	# 	if mas_sel == 0:
	# 		mAdown()		

	def sgup():
		global sg
		textosg.delete("1.0","end")
		sg= sg + 0.1
		if sg >= 5:
			sg = 5
		textosg.insert(INSERT, sg )

	def sgdown():
		global sg
		textosg.delete("1.0","end")
		sg= sg - 0.1
		if sg <= 0:
			sg = 0.1		
		textosg.insert(INSERT, sg )

	def foco_fino():
		focos1=Label(root, image=ff, width=100	, height=42)
		focos1.place(x=280 , y =230)

	def foco_grueso():	
		focos1=Label(root, image=fg, width=100	, height=42)
		focos1.place(x=280 , y =230)

	def delgado_gordo():
		global delgado
		global kv
		boton_smallman = Button(root, image = imagen_smallman_yellow , width = 80, height = 50, command = delgado_gordo)
		boton_smallman.place(x=1130 , y = 190)
		boton_bigman = Button(root, image = imagen_bigman , width = 80, height = 50, command = gordo_delgado)
		boton_bigman.place(x=1225 , y = 190)
		delgado = 1
		kv=kv-10
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )

	def gordo_delgado():
		global delgado
		global kv
		boton_smallman = Button(root, image = imagen_smallman , width = 80, height = 50, command = delgado_gordo)
		boton_smallman.place(x=1130 , y = 190)
		boton_bigman = Button(root, image = imagen_bigman_yellow , width = 80, height = 50, command = gordo_delgado)
		boton_bigman.place(x=1225 , y = 190)
		delgado = 1
		kv=kv+10
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		delgado = 0


		


	def to_pa():
		global kv 
		global mA
		global sg
		global delgado

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="yellow", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)

		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)

		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3_yellow , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = to_pa)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = to_pa)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = to_pa)
		boton_directo.place(x=330, y = 670)


		kv= 120
		if delgado == 1:
			kv=kv-10
		mA = 500
		sg=0.02
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def to_lat():
		global kv 
		global mA
		global sg
			
		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="yellow", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = b_mural_pressed)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = directo_pressed)
		boton_directo.place(x=330, y = 670)

		kv = 120
		mA = 500
		sg=0.03
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def pa_cost():
		global kv 
		global mA
		global sg
		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="yellow", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = pa_cost)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = pa_cost)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = pa_cost)
		boton_directo.place(x=330, y = 670)

		kv = 120
		mA = 300
		sg=0.06
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def hombro():
		global kv 
		global mA
		global sg
		global estado_cervical_ap
		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="yellow", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = hombro)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = hombro)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,   command = hombro)
		boton_directo.place(x=330, y = 670)

		kv = 90
		mA = 300
		sg=0.02
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def cerv_ap():
		global kv 
		global mA
		global sg
		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="yellow", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = cerv_ap)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,   command = cerv_ap)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = cerv_ap)
		boton_directo.place(x=330, y = 670)

		kv = 70
		mA = 300
		sg=0.02
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def s_paran():
		global kv 
		global mA
		global sg
		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="yellow", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = cerv_ap)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = cerv_ap)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = cerv_ap)
		boton_directo.place(x=330, y = 670)

		kv = 70
		mA = 400
		sg=0.02
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def craneo_ap():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="yellow", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = s_paran)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = s_paran)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = s_paran)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = craneo_ap)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = craneo_ap)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = craneo_ap)
		boton_directo.place(x=330, y = 670)

		kv = 85
		mA = 400
		sg=0.08
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def craneo_lat():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="yellow", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = craneo_lat)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = craneo_lat)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = craneo_lat)
		boton_directo.place(x=330, y = 670)


		kv = 80
		mA = 400
		sg=0.08
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def abd_simple():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="yellow", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3_yellow , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa_yellow, command = abd_simple)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = abd_simple)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = abd_simple)
		boton_directo.place(x=330, y = 670)

		kv = 95
		mA = 400
		sg=0.2
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def cadera_femur():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="yellow", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa_yellow, command = cadera_femur)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = cadera_femur)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = cadera_femur)
		boton_directo.place(x=330, y = 670)

		kv = 75
		mA = 400
		sg=0.2
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def dorsal_ap():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="yellow", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 =Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3_yellow , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = dorsal_ap)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = dorsal_ap)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = dorsal_ap)
		boton_directo.place(x=330, y = 670)


		kv = 85
		mA = 400
		sg=0.2
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def dorsal_lat():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="yellow", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = dorsal_lat)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = dorsal_lat)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = dorsal_lat)
		boton_directo.place(x=330, y = 670)

		kv = 95
		mA = 300
		sg=0.3
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def lumbar_ap():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="yellow", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3_yellow , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = lumbar_ap)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,   command = lumbar_ap)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = lumbar_ap)
		boton_directo.place(x=330, y = 670)

		kv = 95
		mA = 400
		sg=0.3
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def lumbar_lat():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="yellow", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = lumbar_lat)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = lumbar_lat)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = lumbar_lat)
		boton_directo.place(x=330, y = 670)

		kv = 100
		mA = 400
		sg=0.3
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def hueso_nasal():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="yellow", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = hueso_nasal)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,   command = hueso_nasal)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = hueso_nasal)
		boton_directo.place(x=330, y = 670)
		
		kv = 75
		mA = 250
		sg=0.1
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def sacro_lat():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="yellow", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa_yellow, command = sacro_lat)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,   command = sacro_lat)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = sacro_lat)
		boton_directo.place(x=330, y = 670)
		
		kv = 100
		mA = 250
		sg=0.2
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def rodilla_ap():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="yellow", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = rodilla_ap)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = rodilla_ap)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = rodilla_ap)
		boton_directo.place(x=330, y = 670)

		
		kv = 70
		mA = 300
		sg=0.08
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def tibia_perone():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="yellow", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 =Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa_yellow, command = tibia_perone)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = tibia_perone)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = tibia_perone)
		boton_directo.place(x=330, y = 670)

		
		kv = 60
		mA = 250
		sg=0.08
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def tobillo_lat():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="yellow", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = tobillo_lat)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,   command = tobillo_lat)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,   command = tobillo_lat)
		boton_directo.place(x=330, y = 670)
		
		kv = 60
		mA = 200
		sg=0.08
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def pie_ap():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="yellow", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = pie_ap)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = pie_ap)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,    command = pie_ap)
		boton_directo.place(x=330, y = 670)
		
		kv = 60
		mA = 160
		sg=0.08
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def codo_ap_lat():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="yellow", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap =Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = codo_ap_lat)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = codo_ap_lat)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,    command = codo_ap_lat)
		boton_directo.place(x=330, y = 670)
		
		kv = 55
		mA = 100
		sg=0.08
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def mano_ap_obl():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="yellow", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = mano_ap_obl)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,   command = mano_ap_obl)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,   command = mano_ap_obl)
		boton_directo.place(x=330, y = 670)
		
		kv = 55
		mA = 100
		sg=0.04
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def dedos():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="yellow", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 =      Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = dedos)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,   command = dedos)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,    command = dedos)
		boton_directo.place(x=330, y = 670)
		
		kv = 55
		mA = 50
		sg=0.04
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )

	def muñeca_ap():
		global kv 
		global mA
		global sg

		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="yellow", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = muñeca_ap)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = muñeca_ap)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,    command = muñeca_ap)
		boton_directo.place(x=330, y = 670)
		
		kv = 55
		mA = 100
		sg=0.05
		textokv.delete("1.0","end")
		textokv.insert(INSERT, kv )
		textomA.delete("1.0","end")
		textomA.insert(INSERT, mA )
		textosg.delete("1.0","end")
		textosg.insert(INSERT, sg )
	def b_mesa_pressed():
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa_yellow, command = b_mesa_pressed)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,   command = b_mural_pressed)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = directo_pressed)
		boton_directo.place(x=330, y = 670)

	def b_mural_pressed():
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,   command = b_mural_pressed)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo, command = directo_pressed)
		boton_directo.place(x=330, y = 670)

	def directo_pressed():
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural, command = b_mural_pressed)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,   command = directo_pressed)
		boton_directo.place(x=330, y = 670)

	def cam1_pressed():
		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50,  command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)

	def cam2_pressed():
		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50,  command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
			
	def cam3_pressed():
		boton_cam3 = Button(root, image = imagen_cam3_yellow , width = 80, height = 50,  command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)

	def reset():
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_sens1 = Button(root, image = imagen_sens1, width = 80, height = 50, command = sensibilidad1)
		boton_sens1.place(x=110 , y = 50)
		boton_sens2 = Button(root, image = imagen_sens2 , width = 80, height = 50, command = sensibilidad2)
		boton_sens2.place(x=110 , y = 120)
		boton_sens3 = Button(root, image = imagen_sens3 , width = 80, height = 50, command = sensibilidad3)
		boton_sens3.place(x=110 , y = 190)
		boton_smallman = Button(root, image = imagen_smallman , width = 80, height = 50, command = delgado_gordo)
		boton_smallman.place(x=1130 , y = 190)
		boton_bigman = Button(root, image = imagen_bigman , width = 80, height = 50, command = gordo_delgado)
		boton_bigman.place(x=1225 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural, command = b_mural_pressed)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = directo_pressed)
		boton_directo.place(x=330, y = 670)
		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur =Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural =Button(root,  width = 80, height = 50, image = b_mural,    command = b_mural_pressed)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = directo_pressed)
		boton_directo.place(x=330, y = 670)
		boton_kv_mas = Button(root, text = "kV-mAs" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mAs)
		boton_kv_mas.place(x=10 , y = 260)
		boton_kv_mas_s = Button(root, text = "kV-mA-s" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mA_sg)
		boton_kv_mas_s.place(x=110 , y = 260)
		mAlabel = Label(root, text= 'mAs', font=("Consolas",25), bg="black", fg = "red")
		mAlabel.place(x=850, y= 230)





	def sensibilidad1():
		boton_sens1 = Button(root, image = imagen_sens1_yellow , width = 80, height = 50, command = sensibilidad1)
		boton_sens1.place(x=110 , y = 50)
		boton_sens2 = Button(root, image = imagen_sens2 , width = 80, height = 50, command = sensibilidad2)
		boton_sens2.place(x=110 , y = 120)
		boton_sens3 = Button(root, image = imagen_sens3 , width = 80, height = 50, command = sensibilidad3)
		boton_sens3.place(x=110 , y = 190)

	def sensibilidad2():
		boton_sens1 = Button(root, image = imagen_sens1 , width = 80, height = 50, command = sensibilidad1)
		boton_sens1.place(x=110 , y = 50)
		boton_sens2 = Button(root, image = imagen_sens2_yellow , width = 80, height = 50, command = sensibilidad2)
		boton_sens2.place(x=110 , y = 120)
		boton_sens3 = Button(root, image = imagen_sens3 , width = 80, height = 50, command = sensibilidad3)
		boton_sens3.place(x=110 , y = 190)

	def sensibilidad3():
		boton_sens1 = Button(root, image = imagen_sens1 , width = 80, height = 50, command = sensibilidad1)
		boton_sens1.place(x=110 , y = 50)
		boton_sens2 = Button(root, image = imagen_sens2 , width = 80, height = 50, command = sensibilidad2)
		boton_sens2.place(x=110 , y = 120)
		boton_sens3 = Button(root, image = imagen_sens3_yellow , width = 80, height = 50, command = sensibilidad3)
		boton_sens3.place(x=110 , y = 190)

	def apagar():

		focos1=Label(root, image=black, width=100	, height=42, bg= "black")
		focos1.place(x=280 , y =230)
		telefono_label = Label(root, image=black, bg="black")
		telefono_label.place(x=250 , y =120)
		alarm_display_label = Label(root, image=black, bg="black")
		alarm_display_label.place(x=300 , y =120)
		ready_label = Label(root, image=black, bg="black")
		ready_label.place(x=350 , y =120)

		textokv = Text(root)
		textokv.config( width=3, height=1, font=("Consolas",40), bg="black", fg = "black") 
		textokv.insert(INSERT, kv )
		textokv.place(x=505 , y = 220) 
		kvlabel = Label(root, text="KV", font=("Consolas",25), bg="black", fg = "black")
		kvlabel.place(x=600, y= 230)
		textomA = Text(root)
		textomA.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "black") 
		textomA.insert(INSERT, mA)
		textomA.place(x=730 , y = 220) 
		mAlabel = Label(root, text= 'mAs', font=("Consolas",25), bg="black", fg = "black")
		mAlabel.place(x=850, y= 230)
		mAlabel = Label(root, text='mA', font=("Consolas",30), bg="black", fg = "black")
		mAlabel.place(x=850, y= 230)
		textosg = Text(root)
		textosg.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "black") 
		textosg.insert(INSERT, sg )
		textosg.place(x=935 , y = 220) 
		sglabel = Label(root, text=sin_seg, font=("Consolas",25), bg="black", fg = "black")
		sglabel.place(x=1055, y= 230)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_sens1 = Button(root, image = imagen_sens1, width = 80, height = 50, command = sensibilidad1)
		boton_sens1.place(x=110 , y = 50)
		boton_sens2 = Button(root, image = imagen_sens2 , width = 80, height = 50, command = sensibilidad2)
		boton_sens2.place(x=110 , y = 120)
		boton_sens3 = Button(root, image = imagen_sens3 , width = 80, height = 50, command = sensibilidad3)
		boton_sens3.place(x=110 , y = 190)
		boton_smallman = Button(root, image = imagen_smallman , width = 80, height = 50, command = delgado_gordo)
		boton_smallman.place(x=1130 , y = 190)
		boton_bigman = Button(root, image = imagen_bigman , width = 80, height = 50, command = gordo_delgado)
		boton_bigman.place(x=1225 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural, command = b_mural_pressed)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = directo_pressed)
		boton_directo.place(x=330, y = 670)
		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
		boton_torax_pa.place(x=460 , y = 530)
		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
		boton_torax_lat.place(x=555 , y = 530)
		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
		boton_parrilla_costal.place(x=460, y = 600)
		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
		boton_hombro.place(x=555 , y = 600)
		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
		boton_cervical_ap.place(x=460, y = 670)
		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
		boton_senos_paranasales.place(x=555 , y = 670)
		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
		boton_craneo_ap_pa.place(x=460, y = 740)
		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
		boton_craneo_lateral.place(x=555 , y = 740)
		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
		boton_abdomen_simple.place(x=685 , y = 530)
		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
		boton_cadera_femur.place(x=780 , y = 530)
		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
		boton_dorsal_ap.place(x=685, y = 600)
		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
		boton_dorsal_lat.place(x=780 , y = 600)
		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
		boton_Lumbar_ap.place(x=685, y = 670)
		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
		boton_Lumbar_lat.place(x=780 , y = 670)
		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
		boton_hueso_nasal.place(x=685, y = 740)
		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
		boton_sacro_lateral.place(x=780 , y = 740)
		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
		boton_rodilla_ap.place(x=910 , y = 530)
		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
		boton_tibia_perone.place(x=1005 , y = 530)
		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
		boton_Tobillo_lateral.place(x=910, y = 600)
		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
		boton_pie_ap.place(x=1005 , y = 600)
		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
		boton_codo_ap_lat.place(x=910, y = 670)
		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
		boton_Mano_ap_obl.place(x=1005 , y = 670)
		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
		boton_dedos.place(x=910, y = 740)
		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
		boton_muñecca_ap.place(x=1005 , y = 740)
		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
		boton_cam1.place(x=10 , y = 50)
		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
		boton_cam2.place(x=10 , y = 120)
		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
		boton_cam3.place(x=10 , y = 190)
		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = muñeca_ap)
		boton_b_mesa.place(x=235 , y = 600)
		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = muñeca_ap)
		boton_b_mural.place(x=235, y = 670)
		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = muñeca_ap)
		boton_directo.place(x=330, y = 670)
		boton_kv_mas = Button(root, text = "kV-mAs" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mAs)
		boton_kv_mas.place(x=10 , y = 260)
		boton_kv_mas_s = Button(root, text = "kV-mA-s" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mA_sg)
		boton_kv_mas_s.place(x=110 , y = 260)


			

	def encender():	
		focos1=Label(root, image=ff, width=100	, height=42)
		focos1.place(x=280 , y =230)
		telefono_label = Label(root, image=telefono, bg="black")
		telefono_label.place(x=250 , y =120)
		alarm_display_label = Label(root, image=alarm_display)
		alarm_display_label.place(x=300 , y =120)
		ready_label = Label(root, image=ready, bg="black")
		ready_label.place(x=350 , y =120)

		textokv = Text(root)
		textokv.config( width=3, height=1, font=("Consolas",40), bg="black", fg = "red") 
		textokv.insert(INSERT, kv )
		textokv.place(x=505 , y = 220) 
		kvlabel = Label(root, text="KV", font=("Consolas",25), bg="black", fg = "red")
		kvlabel.place(x=600, y= 230)
		textomA = Text(root)
		textomA.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "red") 
		textomA.insert(INSERT, mA)
		textomA.place(x=730 , y = 220) 
		mAlabel = Label(root, text='mA', font=("Consolas",25), bg="black", fg = "red")
		mAlabel.place(x=850, y= 230)
		textosg = Text(root)
		textosg.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "red") 
		textosg.insert(INSERT, sg )
		textosg.place(x=935 , y = 220) 
		sglabel = Label(root, text=sin_seg, font=("Consolas",25), bg="black", fg = "red")
		sglabel.place(x=1055, y= 230)
		telefono_label = Label(root, image=black, bg="black")
		telefono_label.place(x=250 , y =120)
		alarm_display_label = Label(root, image=black)
		alarm_display_label.place(x=300 , y =120)

	root = Toplevel()
	
	ancho_ventana = 1325
	alto_ventana = 850


	x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
	y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

	posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana-90)
	root.geometry(posicion)

	root.resizable(0,0)
	# root.geometry("1325x850")
	# root.resizable(0,0)
	root.title("                                                                                                                             SIMULADOR CONSOLA MEDIO CP PHILIPS REALIZADO POR XRAY SERVICE SOLUTIONS")
	#root.iconbitmap('C:/master_python/xray_ide/Consola1ph/xray.ico')

	imagen_ff = PhotoImage(file=f'{cwd}/imagen_ff.png')
	imagen_fg = PhotoImage(file=f'{cwd}/imagen_fg.png')
	imagen_cam1 = PhotoImage(file=f'{cwd}/cam1.png')
	imagen_cam2 = PhotoImage(file=f'{cwd}/cam2.png')
	imagen_cam3 = PhotoImage(file=f'{cwd}/cam3.png')
	imagen_cam1_yellow = PhotoImage(file=f'{cwd}/cam1yellow.png')
	imagen_cam2_yellow = PhotoImage(file=f'{cwd}/cam2yellow.png')
	imagen_cam3_yellow = PhotoImage(file=f'{cwd}/cam3yellow.png')



	imagen_sens1 = PhotoImage(file=f'{cwd}/sens1.png')
	imagen_sens2 = PhotoImage(file=f'{cwd}/sens2.png')
	imagen_sens3 = PhotoImage(file=f'{cwd}/sens3.png')
	imagen_sens1_yellow = PhotoImage(file=f'{cwd}/sens1_yellow.png')
	imagen_sens2_yellow = PhotoImage(file=f'{cwd}/sens2_yellow.png')
	imagen_sens3_yellow = PhotoImage(file=f'{cwd}/sens3_yellow.png')
	imagen_shoot = PhotoImage(file=f'{cwd}/simbolorx.png')
	imagen_alarm = PhotoImage(file=f'{cwd}/alarm.png')
	imagen_smallman = PhotoImage(file=f'{cwd}/smallman.png')
	imagen_bigman = PhotoImage(file=f'{cwd}/bigman.png')
	imagen_smallman_yellow = PhotoImage(file=f'{cwd}/smallman_yellow.png')
	imagen_bigman_yellow = PhotoImage(file=f'{cwd}/bigman_yellow.png')
	b_mesa = PhotoImage(file=f'{cwd}/b_mesa.png')
	b_mural = PhotoImage(file=f'{cwd}/b_mural.png')
	directo = PhotoImage(file=f'{cwd}/directo.png')
	b_mesa_yellow = PhotoImage(file=f'{cwd}/b_mesa_yellow.png')
	b_mural_yellow = PhotoImage(file=f'{cwd}/b_mural_yellow.png')
	directo_yellow = PhotoImage(file=f'{cwd}/directo_yellow.png')
	on = PhotoImage(file=f'{cwd}/on.png')
	off = PhotoImage(file=f'{cwd}/off.png')
	shoot = PhotoImage(file=f'{cwd}/disparo.png')
	black = PhotoImage(file=f'{cwd}/black.png')
	ff = PhotoImage(file=f'{cwd}/ff.png')
	fg = PhotoImage(file=f'{cwd}/fg.png')
	ready = PhotoImage(file=f'{cwd}/ready.png')
	alarm_display = PhotoImage(file=f'{cwd}/alarm_display.png')
	telefono = PhotoImage(file=f'{cwd}/telefono.png')





	frame_display = Frame(root, width = 885 , height = 200 , bg = "black") 
	frame_display.place (x=220 , y =100)
	focos1=Label(root, image=ff, width=100	, height=42)
	focos1.place(x=280 , y =230)
	boton_ff = Button(root , width = 80, height = 50, image = imagen_ff, command = foco_fino)
	boton_ff.place(x=235 , y = 320)
	boton_fg = Button(root,  width = 80, height = 50, image = imagen_fg,  command = foco_grueso)
	boton_fg.place(x=330, y = 320)
	telefono_label = Label(root, image=black, bg="black")
	telefono_label.place(x=250 , y =120)
	alarm_display_label = Label(root, image=black)
	alarm_display_label.place(x=300 , y =120)
	ready_label = Label(root, image=ready, bg="black")
	ready_label.place(x=350 , y =120)

	textokv = Text(root)
	textokv.config( width=3, height=1, font=("Consolas",40), bg="black", fg = "red") 
	textokv.insert(INSERT, kv )
	textokv.place(x=505 , y = 220) 
	kvlabel = Label(root, text="KV", font=("Consolas",25), bg="black", fg = "red")
	kvlabel.place(x=600, y= 230)
	boton_bajarkv = Button(root, text = "-" , width = 5, height = 1,bg ="white", font=("Consolas",20))
	boton_bajarkv.place(x=460 , y = 320)
	boton_bajarkv.bind('<Button-1>', lambda e: Thread(target=click_kv_cont_down, daemon=True).start())
	boton_bajarkv.bind('<ButtonRelease-1>', release_kv_cont_down)
	boton_subirkv = Button(root, text = "+", width = 5, height = 1,bg ="white", font=("Consolas",20))
	boton_subirkv.place(x=555, y = 320)
	boton_subirkv.bind('<Button-1>', lambda e: Thread(target=click_kv_cont_up, daemon=True).start())
	boton_subirkv.bind('<ButtonRelease-1>', release_kv_cont_up)

	textomA = Text(root)
	textomA.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "red") 
	textomA.insert(INSERT, mA)
	textomA.place(x=730 , y = 220) 
	mAlabel = Label(root, text='mA', font=("Consolas",25), bg="black", fg = "red")
	mAlabel.place(x=850, y= 230)

	boton_bajarmA = Button(root, text = "-" , width =5, height = 1,bg ="white", font=("Consolas",20), command = mAdown)
	boton_bajarmA.place(x=685 , y = 320)
	boton_subirmA = Button(root, text = "+", width = 5, height = 1,bg ="white", font=("Consolas",20),  command = mAup)
	boton_subirmA.place(x=780, y = 320)

	textosg = Text(root)
	textosg.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "red") 
	textosg.insert(INSERT, sg )
	textosg.place(x=935 , y = 220) 
	sglabel = Label(root, text=sin_seg, font=("Consolas",25), bg="black", fg = "red")
	sglabel.place(x=1055, y= 230)
	boton_bajarsg = Button(root, text = "-" , width = 5, height = 1,bg ="white", font=("Consolas",20), command = sgdown)
	boton_bajarsg.place(x=910 , y = 320)
	boton_subirsg = Button(root, text = "+", width = 5, height = 1,bg ="white", font=("Consolas",20),  command = sgup)
	boton_subirsg.place(x=1005, y = 320)
	boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
	boton_cam1.place(x=10 , y = 50)
	boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
	boton_cam2.place(x=10 , y = 120)
	boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
	boton_cam3.place(x=10 , y = 190)
	boton_kv_mas = Button(root, text = "kV-mAs" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mAs)
	boton_kv_mas.place(x=10 , y = 260)

	boton_sens1 = Button(root, image = imagen_sens1 , width = 80, height = 50, command = sensibilidad1)
	boton_sens1.place(x=110 , y = 50)
	boton_sens2 = Button(root, image = imagen_sens2 , width = 80, height = 50, command = sensibilidad2)
	boton_sens2.place(x=110 , y = 120)
	boton_sens3 = Button(root, image = imagen_sens3 , width = 80, height = 50, command = sensibilidad3)
	boton_sens3.place(x=110 , y = 190)
	boton_kv_mas_s = Button(root, text = "kV-mA-s" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mA_sg)
	boton_kv_mas_s.place(x=110 , y = 260)

	boton_reset = Button(root, text = "Reset" , width = 11, height = 3, bg ="white", command = reset)
	boton_reset.place(x=1130 , y = 50)
	boton_alarm = Button(root, image = imagen_alarm , width = 80, height = 50, command = alarm_off)
	boton_alarm.place(x=1225 , y = 50)
	boton_smallman = Button(root, image = imagen_smallman , width = 80, height = 50, command = delgado_gordo)
	boton_smallman.place(x=1130 , y = 190)
	boton_bigman = Button(root, image = imagen_bigman , width = 80, height = 50, command = gordo_delgado)
	boton_bigman.place(x=1225 , y = 190)

	boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
	boton_b_mesa.place(x=235 , y = 600)
	boton_libre1 = Button(root,  width = 11, height = 3, bg ="white",  command = sgup)
	boton_libre1.place(x=330, y = 600)
	boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural, bg ="white",   command = b_mural_pressed)
	boton_b_mural.place(x=235, y = 670)
	boton_directo = Button(root,  width = 80, height = 50,image = directo, bg ="white",   command = directo_pressed)
	boton_directo.place(x=330, y = 670)
	boton_libre2 = Button(root,  width = 11, height = 3, bg ="white",   command = sgup)
	boton_libre2.place(x=235, y = 740)
	boton_libre3 = Button(root,  width = 11, height = 3, bg ="white",   command = sgup)
	boton_libre3.place(x=330, y = 740)

	boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
	boton_torax_pa.place(x=460 , y = 530)
	boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
	boton_torax_lat.place(x=555 , y = 530)
	boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
	boton_parrilla_costal.place(x=460, y = 600)
	boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
	boton_hombro.place(x=555 , y = 600)
	boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
	boton_cervical_ap.place(x=460, y = 670)
	boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
	boton_senos_paranasales.place(x=555 , y = 670)
	boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
	boton_craneo_ap_pa.place(x=460, y = 740)
	boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
	boton_craneo_lateral.place(x=555 , y = 740)

	boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
	boton_abdomen_simple.place(x=685 , y = 530)
	boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
	boton_cadera_femur.place(x=780 , y = 530)
	boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
	boton_dorsal_ap.place(x=685, y = 600)
	boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
	boton_dorsal_lat.place(x=780 , y = 600)
	boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
	boton_Lumbar_ap.place(x=685, y = 670)
	boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
	boton_Lumbar_lat.place(x=780 , y = 670)
	boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
	boton_hueso_nasal.place(x=685, y = 740)
	boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
	boton_sacro_lateral.place(x=780 , y = 740)

	boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
	boton_rodilla_ap.place(x=910 , y = 530)
	boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
	boton_tibia_perone.place(x=1005 , y = 530)
	boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
	boton_Tobillo_lateral.place(x=910, y = 600)
	boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
	boton_pie_ap.place(x=1005 , y = 600)
	boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
	boton_codo_ap_lat.place(x=910, y = 670)
	boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
	boton_Mano_ap_obl.place(x=1005 , y = 670)
	boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
	boton_dedos.place(x=910, y = 740)
	boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
	boton_muñecca_ap.place(x=1005 , y = 740)

	boton_on = Button(root , width = 80, height = 50, image = on, command = encender)
	boton_on.place(x=10 , y = 600)
	boton_off = Button(root , width = 160, height = 50, image = off, command = apagar)
	boton_off.place(x=10 , y = 740)
	boton_shoot = Button(root , width = 50, height = 50, image = shoot)
	boton_shoot.place(x=1177 , y = 740)
	boton_shoot.bind('<Button-1>', lambda e: Thread(target=click_shoot, daemon=True).start())
	boton_shoot.bind('<ButtonRelease-1>', release_shoot)
	splabel = Label(root, text="  ", font=("Consolas",25), bg="grey", fg = "red")
	splabel.place(x=1120, y= 745)
	splabel = Label(root, text="  ", font=("Consolas",25), bg="grey", fg = "red")
	splabel.place(x=1250, y= 745)

	root.mainloop()
# skv = int()
# skv = 40
# smA = int()
# smA = 10
# ssg = float()
# ssg = 0.10
# sfs = float()
# sfs = 40
# sct = int()
# sct = 0
# scm = int()
# scm = 0
# spuntos = str()
# spuntos = 'mA'
# ssin_seg = str()
# ssin_seg = 'sg'
# smiliseg = float()
# smas_sel = 0
# smAs_calc = float()
# smAs = float()
# sdelgado = 0
# sreleasekvdown = True
# sreleasekvup = True
# sreleaseshoot = True
# sfrequency = int()
# sduration = int()
# sestado_torax_pa = 0
# sestado_torax_lat = 0
# sestado_parrilla_costal = 0
# sestado_hombro = 0
# sestado_cervical_ap = 0
# sestado_s_paranasales = 0
# sestado_craneo_pa = 0
# sestado_craneo_lat = 0
# sestado_abdomen_simple = 0
# sestado_cadera_femur = 0
# sestado_dorsal_ap = 0
# sestado_dorsal_lat = 0
# sestado_lumbar_ap = 0
# sestado_lumbar_lat = 0
# sestado_hueso_nasal = 0
# sestado_sacro_lat = 0
# sestado_rodilla_ap = 0
# sestado_tibia_perone = 0
# sestado_tobillo_lat = 0
# sestado_pie_ap = 0
# sestado_codo_ap = 0
# sestado_mano_ap = 0
# sestado_dedos = 0
# sestado_muñeca = 0
# scontador_alarma = 0
# scontador_servicio = 0
# def sedecal():
# 	def click_kv_cont_down():
# 		global skv
# 		global sreleasekvdown
# 		sreleasekvdown = False
# 		while not sreleasekvdown:
# 			time.sleep(0.3)
# 			textokv.delete("1.0","end")
# 			if skv== 40:
# 				skv=skv
# 			else:
# 				skv=skv-1	
# 			textokv.insert(INSERT, skv )
		
# 	def release_kv_cont_down(e):
# 		global sreleasekvdown
# 		sreleasekvdown = True

# 	def click_kv_cont_up():
# 		global skv
# 		global sreleasekvup
# 		sreleasekvup = False
# 		while not sreleasekvup:
# 			time.sleep(0.3)
# 			textokv.delete("1.0","end")
# 			if skv==150:
# 				skv=skv
# 			else:
# 				skv= skv + 1
# 			textokv.insert(INSERT, skv )


# 	def release_kv_cont_up(e):
# 		global sreleasekvup
# 		sreleasekvup = True

# 	def click_shoot():
# 		global sfrequency
# 		global sduration
# 		global sreleaseshoot
# 		global ssg
# 		global scontador_alarma
# 		global scontador_servicio
# 		sreleaseshoot = False

# 		if not sreleaseshoot:
			

# 			rxon=Label(root, image=imagen_shoot, bg="black")
# 			rxon.place(x=400 , y =120) 
# 			frequency = 2000
# 			duration = int(sg*1000)
# 			winsound.Beep(frequency, duration)
# 			rxon=Label(root, image=black, bg ="black")
# 			rxon.place(x=400 , y =120) 
# 			contador_alarma = contador_alarma + 1
# 			if contador_alarma >= 8 :
# 				alarma_on()
# 			contador_servicio = random.randint(1, 10)
		
# 			if contador_servicio == 2:
# 				frequency = 3000
# 				duration = 1000000
# 				telefono_label = Label(root, image=telefono, bg="black")
# 				telefono_label.place(x=250 , y =120)
# 				time.sleep(1)
# 				alarma_on()
# 			else:
# 				frequency = 800

# 	def alarma_on():
# 		global duration
# 		global frequency
# 		global contador_servicio
# 		global duration
# 		ready_label = Label(root, image=black, bg="black")
# 		ready_label.place(x=350 , y =120)
		

# 		duration = int(1000000)
# 		alarm_display_label = Label(root, image=alarm_display)
# 		alarm_display_label.place(x=300 , y =120)
# 		winsound.Beep(frequency, duration)

# 	def alarm_off():
# 		global duration
# 		global frequency
# 		global contador_alarma
# 		ready_label = Label(root, image=ready, bg="black")
# 		ready_label.place(x=350 , y =120)
# 		frequency = 800
# 		duration = int(0)
# 		alarm_display_label = Label(root, image=black)
# 		alarm_display_label.place(x=300 , y =120)
# 		winsound.Beep(frequency, duration)
# 		telefono_label = Label(root, image=black, bg="black")
# 		telefono_label.place(x=250 , y =120)
# 		contador_alarma = 0



			

# 	def release_shoot(e):
# 		global sreleaseshoot
# 		time.sleep(0.1)
# 		sreleaseshoot = True
# 		rxon=Label(root, image=black, width=30	, height=30)
# 		rxon.place(x=400 , y =120) 

# 	def kv_mAs():
# 		global smas_sel
# 		global spuntos
# 		global ssg
# 		global smiliseg
# 		global smA
# 		miliseg =smA*ssg
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, miliseg )	
# 		smas_sel = 1
# 		mAlabel = Label(root, text= 'mAs', font=("Consolas",25), bg="black", fg = "red")
# 		mAlabel.place(x=850, y= 230)
# 		puntos = 'mA'
# 		mAlabel = Label(root, text=puntos, font=("Consolas",25), bg="black", fg = "red")
# 		mAlabel.place(x=850, y= 230)
# 		textosg.config( width=5, height=1, font=("Consolas",25), bg="black", fg = "black") 
# 		textosg.insert(INSERT, sg)
# 		textosg.place(x=935 , y = 220) 
# 		sglabel = Label(root, text='  ', font=("Consolas",25), bg="black", fg = "red")
# 		sglabel.place(x=1055, y= 230)
# 		boton_kv_mas = Button(root, text = "kV-mAs" , width = 11, height = 3, font=("Consolas",10),bg ="yellow", command = kv_mAs)
# 		boton_kv_mas.place(x=10 , y = 260)
# 		boton_kv_mas_s = Button(root, text = "kV-mA-s" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mA_sg)
# 		boton_kv_mas_s.place(x=110 , y = 260)
# 	def kv_mA_sg():
# 		global smas_sel
# 		global spuntos
# 		global ssg
# 		global smA
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		smas_sel = 0
# 		puntos = '    '
# 		mAlabel = Label(root, text= puntos, font=("Consolas",25), bg="black", fg = "red")
# 		mAlabel.place(x=850, y= 230)
# 		puntos = 'mA'
# 		mAlabel = Label(root, text='mA', font=("Consolas",25), bg="black", fg = "red")
# 		mAlabel.place(x=850, y= 230)
# 		textosg.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "red") 
# 		textosg.insert(INSERT, sg)
# 		textosg.place(x=935 , y = 220) 
# 		sglabel = Label(root, text='sg', font=("Consolas",25), bg="black", fg = "red")
# 		sglabel.place(x=1055, y= 230)
# 		boton_kv_mas = Button(root, text = "kV-mAs" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mAs)
# 		boton_kv_mas.place(x=10 , y = 260)
# 		boton_kv_mas_s = Button(root, text = "kV-mA-s" , width = 11, height = 3, font=("Consolas",10),bg ="yellow", command = kv_mA_sg)
# 		boton_kv_mas_s.place(x=110 , y = 260)



# 	def mAup():
# 		global smA
# 		global sct
# 		global smas_sel
# 		if smas_sel == 0:

# 			smA = 10
# 			if sct == 0:
# 				smA = 16
# 			elif sct == 1:
# 				smA = 25
# 			elif sct == 2:
# 				smA = 50
# 			elif sct == 3:
# 				smA = 100
# 			elif sct == 4:
# 				smA = 160
# 			elif sct == 5:
# 				smA = 200
# 			elif sct == 6:
# 				smA = 250
# 			elif sct == 7:
# 				smA = 300
# 			elif sct == 8:
# 				smA = 350
# 			elif sct == 9:
# 				smA = 400
# 			elif sct == 10:
# 				smA = 500		
# 			sct = sct +1
# 			if sct >=11:
# 				sct=0
# 				smA=smA
# 			textomA.delete("1.0","end")
# 			textomA.insert(INSERT, smA )
# 		else:
# 			mAs_up_sel()		

# 	def mAdown():
		
# 		global smA
# 		global smas_sel
# 		if smas_sel == 0:
		
# 			if smA == 500:
# 				smA = 400
# 			elif smA == 400:
# 				smA = 350
# 			elif smA == 350:
# 				smA = 300
# 			elif smA == 300:
# 				smA = 250
# 			elif smA == 250:
# 				smA = 200
# 			elif smA == 200:
# 				smA = 160
# 			elif smA == 160:
# 				smA = 100
# 			elif smA == 100:
# 				smA = 50
# 			elif smA == 50:
# 				smA = 25
# 			elif smA == 25:
# 				smA=16
# 			elif smA == 16:
# 				smA=10
# 			textomA.delete("1.0","end")
# 			textomA.insert(INSERT, smA )	

# 		else:

# 			mAs_down_sel()

# 	def mAs_up_sel():
# 		global scm
# 		global smAs
# 		global smiliseg
# 		global ssg
# 		global smA	

# 		if scm == 0:
# 			smiliseg = smA*ssg
# 		elif scm == 1:
# 			smiliseg = 25*0.1
# 		elif scm == 2:
# 			smiliseg = 50*0.1
# 		elif scm == 3:
# 			smiliseg = 100*0.1
# 		elif scm == 4:
# 			smiliseg = 160*0.1
# 		elif scm == 5:
# 			smiliseg = 200*0.1
# 		elif scm == 6:
# 			smiliseg = 250*0.1
# 		elif scm == 7:
# 			smiliseg = 300*0.1
# 		elif scm == 8:
# 			smiliseg = 350*0.1
# 		elif scm == 9:
# 			smiliseg = 400*0.1
# 		elif scm == 10:
# 			smiliseg = 500*0.1		
# 		scm = scm +1
# 		if scm >=11:
# 			scm=0
		
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smiliseg )

# 	def mAs_down_sel():
		
# 		global scm
# 		global smAs
# 		global smiliseg
# 		global ssg
# 		global smA	

# 		if scm == 0:
# 			smiliseg = smA*ssg
# 		elif scm == 1:
# 			smiliseg = 500*0.1
# 		elif scm == 2:
# 			smiliseg = 400*0.1
# 		elif scm == 3:
# 			smiliseg = 350*0.1
# 		elif scm == 4:
# 			smiliseg = 300*0.1
# 		elif scm == 5:
# 			smiliseg = 250*0.1
# 		elif scm == 6:
# 			smiliseg = 200*0.1
# 		elif scm == 7:
# 			smiliseg = 160*0.1
# 		elif scm == 8:
# 			smiliseg = 100*0.1
# 		elif scm == 9:
# 			smiliseg = 50*0.1
# 		elif scm == 10:
# 			smiliseg = 25*0.1		
# 		scm = scm +1
# 		if scm >=11:
# 			scm=0
		
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smiliseg )

# 	def mAs_down():
# 		global smas_sel
# 		if smas_sel == 0:
# 			mAdown()		

# 	def sgup():
# 		global ssg
# 		textosg.delete("1.0","end")
# 		ssg= sg + 0.1
# 		if ssg >= 5:
# 			ssg = 5
# 		textosg.insert(INSERT, ssg )

# 	def sgdown():
# 		global ssg
# 		textosg.delete("1.0","end")
# 		ssg= ssg - 0.1
# 		if ssg <= 0:
# 			ssg = 0.1		
# 		textosg.insert(INSERT, ssg )

# 	def foco_fino():
# 		focos1=Label(root, image=ff, width=100	, height=42)
# 		focos1.place(x=280 , y =230)

# 	def foco_grueso():	
# 		focos1=Label(root, image=fg, width=100	, height=42)
# 		focos1.place(x=280 , y =230)

# 	def delgado_gordo():
# 		global sdelgado
# 		global skv
# 		boton_smallman = Button(root, image = imagen_smallman_yellow , width = 80, height = 50, command = delgado_gordo)
# 		boton_smallman.place(x=1130 , y = 190)
# 		boton_bigman = Button(root, image = imagen_bigman , width = 80, height = 50, command = gordo_delgado)
# 		boton_bigman.place(x=1225 , y = 190)
# 		sdelgado = 1
# 		skv=skv-10
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )

# 	def gordo_delgado():
# 		global sdelgado
# 		global skv
# 		boton_smallman = Button(root, image = imagen_smallman , width = 80, height = 50, command = delgado_gordo)
# 		boton_smallman.place(x=1130 , y = 190)
# 		boton_bigman = Button(root, image = imagen_bigman_yellow , width = 80, height = 50, command = gordo_delgado)
# 		boton_bigman.place(x=1225 , y = 190)
# 		sdelgado = 1
# 		skv=skv+10
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		sdelgado = 0


		


# 	def to_pa():
# 		global skv 
# 		global smA
# 		global ssg
# 		global sdelgado

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="yellow", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)

# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)

# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3_yellow , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = to_pa)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = to_pa)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = to_pa)
# 		boton_directo.place(x=330, y = 670)


# 		skv= 120
# 		if sdelgado == 1:
# 			skv=skv-10
# 		smA = 500
# 		ssg=0.02
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def to_lat():
# 		global skv 
# 		global smA
# 		global ssg
			
# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="yellow", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = b_mural_pressed)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = directo_pressed)
# 		boton_directo.place(x=330, y = 670)

# 		skv = 120
# 		smA = 500
# 		ssg=0.03
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def pa_cost():
# 		global skv 
# 		global smA
# 		global ssg
# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="yellow", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = pa_cost)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = pa_cost)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = pa_cost)
# 		boton_directo.place(x=330, y = 670)

# 		skv = 120
# 		smA = 300
# 		ssg=0.06
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def hombro():
# 		global skv 
# 		global smA
# 		global ssg
# 		global sestado_cervical_ap
# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="yellow", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = hombro)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = hombro)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,   command = hombro)
# 		boton_directo.place(x=330, y = 670)

# 		skv = 90
# 		smA = 300
# 		ssg=0.02
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def cerv_ap():
# 		global skv 
# 		global smA
# 		global ssg
# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="yellow", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = cerv_ap)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,   command = cerv_ap)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = cerv_ap)
# 		boton_directo.place(x=330, y = 670)

# 		skv = 70
# 		smA = 300
# 		ssg=0.02
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def s_paran():
# 		global skv 
# 		global smA
# 		global ssg
# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="yellow", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = cerv_ap)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = cerv_ap)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = cerv_ap)
# 		boton_directo.place(x=330, y = 670)

# 		skv = 70
# 		smA = 400
# 		ssg=0.02
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def craneo_ap():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="yellow", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = s_paran)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = s_paran)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = s_paran)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = craneo_ap)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = craneo_ap)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = craneo_ap)
# 		boton_directo.place(x=330, y = 670)

# 		skv = 85
# 		smA = 400
# 		ssg=0.08
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def craneo_lat():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="yellow", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = craneo_lat)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = craneo_lat)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = craneo_lat)
# 		boton_directo.place(x=330, y = 670)


# 		skv = 80
# 		smA = 400
# 		ssg=0.08
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def abd_simple():
# 		global skv 
# 		global ssmA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="yellow", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3_yellow , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa_yellow, command = abd_simple)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = abd_simple)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = abd_simple)
# 		boton_directo.place(x=330, y = 670)

# 		skv = 95
# 		smA = 400
# 		ssg=0.2
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def cadera_femur():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="yellow", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa_yellow, command = cadera_femur)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = cadera_femur)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = cadera_femur)
# 		boton_directo.place(x=330, y = 670)

# 		skv = 75
# 		smA = 400
# 		ssg=0.2
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def dorsal_ap():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="yellow", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 =Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3_yellow , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = dorsal_ap)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = dorsal_ap)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = dorsal_ap)
# 		boton_directo.place(x=330, y = 670)


# 		skv = 85
# 		smA = 400
# 		ssg=0.2
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def dorsal_lat():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="yellow", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = dorsal_lat)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = dorsal_lat)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = dorsal_lat)
# 		boton_directo.place(x=330, y = 670)

# 		skv = 95
# 		smA = 300
# 		ssg=0.3
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def lumbar_ap():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="yellow", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3_yellow , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = lumbar_ap)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,   command = lumbar_ap)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = lumbar_ap)
# 		boton_directo.place(x=330, y = 670)

# 		skv = 95
# 		smA = 400
# 		ssg=0.3
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def lumbar_lat():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="yellow", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = lumbar_lat)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = lumbar_lat)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = lumbar_lat)
# 		boton_directo.place(x=330, y = 670)

# 		skv = 100
# 		smA = 400
# 		ssg=0.3
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, sssg )

# 	def hueso_nasal():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="yellow", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = hueso_nasal)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,   command = hueso_nasal)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = hueso_nasal)
# 		boton_directo.place(x=330, y = 670)
		
# 		skv = 75
# 		smA = 250
# 		ssg=0.1
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def sacro_lat():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="yellow", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa_yellow, command = sacro_lat)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,   command = sacro_lat)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = sacro_lat)
# 		boton_directo.place(x=330, y = 670)
		
# 		skv = 100
# 		smA = 250
# 		ssg=0.2
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def rodilla_ap():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="yellow", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = rodilla_ap)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,    command = rodilla_ap)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = rodilla_ap)
# 		boton_directo.place(x=330, y = 670)

		
# 		skv = 70
# 		smA = 300
# 		ssg=0.08
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def tibia_perone():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="yellow", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 =Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa_yellow, command = tibia_perone)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = tibia_perone)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = tibia_perone)
# 		boton_directo.place(x=330, y = 670)

		
# 		skv = 60
# 		smA = 250
# 		ssg=0.08
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def tobillo_lat():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="yellow", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = tobillo_lat)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,   command = tobillo_lat)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,   command = tobillo_lat)
# 		boton_directo.place(x=330, y = 670)
		
# 		skv = 60
# 		smA = 200
# 		ssg=0.08
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def pie_ap():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="yellow", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = pie_ap)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = pie_ap)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,    command = pie_ap)
# 		boton_directo.place(x=330, y = 670)
		
# 		skv = 60
# 		smA = 160
# 		ssg=0.08
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def codo_ap_lat():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="yellow", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap =Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = codo_ap_lat)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = codo_ap_lat)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,    command = codo_ap_lat)
# 		boton_directo.place(x=330, y = 670)
		
# 		skv = 55
# 		smA = 100
# 		ssg=0.08
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def mano_ap_obl():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="yellow", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = mano_ap_obl)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,   command = mano_ap_obl)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,   command = mano_ap_obl)
# 		boton_directo.place(x=330, y = 670)
		
# 		skv = 55
# 		smA = 100
# 		ssg=0.04
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def dedos():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="yellow", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 =      Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = dedos)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,   command = dedos)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,    command = dedos)
# 		boton_directo.place(x=330, y = 670)
		
# 		skv = 55
# 		smA = 50
# 		ssg=0.04
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )

# 	def muñeca_ap():
# 		global skv 
# 		global smA
# 		global ssg

# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="yellow", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = muñeca_ap)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = muñeca_ap)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,    command = muñeca_ap)
# 		boton_directo.place(x=330, y = 670)
		
# 		skv = 55
# 		smA = 100
# 		ssg=0.05
# 		textokv.delete("1.0","end")
# 		textokv.insert(INSERT, skv )
# 		textomA.delete("1.0","end")
# 		textomA.insert(INSERT, smA )
# 		textosg.delete("1.0","end")
# 		textosg.insert(INSERT, ssg )
# 	def b_mesa_pressed():
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa_yellow, command = b_mesa_pressed)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,   command = b_mural_pressed)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = directo_pressed)
# 		boton_directo.place(x=330, y = 670)

# 	def b_mural_pressed():
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural_yellow,   command = b_mural_pressed)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo, command = directo_pressed)
# 		boton_directo.place(x=330, y = 670)

# 	def directo_pressed():
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural, command = b_mural_pressed)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo_yellow,   command = directo_pressed)
# 		boton_directo.place(x=330, y = 670)

# 	def cam1_pressed():
# 		boton_cam1 = Button(root, image = imagen_cam1_yellow , width = 80, height = 50,  command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)

# 	def cam2_pressed():
# 		boton_cam2 = Button(root, image = imagen_cam2_yellow , width = 80, height = 50,  command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
			
# 	def cam3_pressed():
# 		boton_cam3 = Button(root, image = imagen_cam3_yellow , width = 80, height = 50,  command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)

# 	def reset():
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_sens1 = Button(root, image = imagen_sens1, width = 80, height = 50, command = sensibilidad1)
# 		boton_sens1.place(x=110 , y = 50)
# 		boton_sens2 = Button(root, image = imagen_sens2 , width = 80, height = 50, command = sensibilidad2)
# 		boton_sens2.place(x=110 , y = 120)
# 		boton_sens3 = Button(root, image = imagen_sens3 , width = 80, height = 50, command = sensibilidad3)
# 		boton_sens3.place(x=110 , y = 190)
# 		boton_smallman = Button(root, image = imagen_smallman , width = 80, height = 50, command = delgado_gordo)
# 		boton_smallman.place(x=1130 , y = 190)
# 		boton_bigman = Button(root, image = imagen_bigman , width = 80, height = 50, command = gordo_delgado)
# 		boton_bigman.place(x=1225 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural, command = b_mural_pressed)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = directo_pressed)
# 		boton_directo.place(x=330, y = 670)
# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur =Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural =Button(root,  width = 80, height = 50, image = b_mural,    command = b_mural_pressed)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = directo_pressed)
# 		boton_directo.place(x=330, y = 670)
# 		boton_kv_mas = Button(root, text = "kV-mAs" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mAs)
# 		boton_kv_mas.place(x=10 , y = 260)
# 		boton_kv_mas_s = Button(root, text = "kV-mA-s" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mA_sg)
# 		boton_kv_mas_s.place(x=110 , y = 260)
# 		mAlabel = Label(root, text= 'mAs', font=("Consolas",25), bg="black", fg = "red")
# 		mAlabel.place(x=850, y= 230)





# 	def sensibilidad1():
# 		boton_sens1 = Button(root, image = imagen_sens1_yellow , width = 80, height = 50, command = sensibilidad1)
# 		boton_sens1.place(x=110 , y = 50)
# 		boton_sens2 = Button(root, image = imagen_sens2 , width = 80, height = 50, command = sensibilidad2)
# 		boton_sens2.place(x=110 , y = 120)
# 		boton_sens3 = Button(root, image = imagen_sens3 , width = 80, height = 50, command = sensibilidad3)
# 		boton_sens3.place(x=110 , y = 190)

# 	def sensibilidad2():
# 		boton_sens1 = Button(root, image = imagen_sens1 , width = 80, height = 50, command = sensibilidad1)
# 		boton_sens1.place(x=110 , y = 50)
# 		boton_sens2 = Button(root, image = imagen_sens2_yellow , width = 80, height = 50, command = sensibilidad2)
# 		boton_sens2.place(x=110 , y = 120)
# 		boton_sens3 = Button(root, image = imagen_sens3 , width = 80, height = 50, command = sensibilidad3)
# 		boton_sens3.place(x=110 , y = 190)

# 	def sensibilidad3():
# 		boton_sens1 = Button(root, image = imagen_sens1 , width = 80, height = 50, command = sensibilidad1)
# 		boton_sens1.place(x=110 , y = 50)
# 		boton_sens2 = Button(root, image = imagen_sens2 , width = 80, height = 50, command = sensibilidad2)
# 		boton_sens2.place(x=110 , y = 120)
# 		boton_sens3 = Button(root, image = imagen_sens3_yellow , width = 80, height = 50, command = sensibilidad3)
# 		boton_sens3.place(x=110 , y = 190)

# 	def apagar():

# 		focos1=Label(root, image=black, width=100	, height=42, bg= "black")
# 		focos1.place(x=280 , y =230)
# 		telefono_label = Label(root, image=black, bg="black")
# 		telefono_label.place(x=250 , y =120)
# 		alarm_display_label = Label(root, image=black, bg="black")
# 		alarm_display_label.place(x=300 , y =120)
# 		ready_label = Label(root, image=black, bg="black")
# 		ready_label.place(x=350 , y =120)

# 		textokv = Text(root)
# 		textokv.config( width=3, height=1, font=("Consolas",40), bg="black", fg = "black") 
# 		textokv.insert(INSERT, kv )
# 		textokv.place(x=505 , y = 220) 
# 		kvlabel = Label(root, text="KV", font=("Consolas",25), bg="black", fg = "black")
# 		kvlabel.place(x=600, y= 230)
# 		textomA = Text(root)
# 		textomA.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "black") 
# 		textomA.insert(INSERT, mA)
# 		textomA.place(x=730 , y = 220) 
# 		mAlabel = Label(root, text= 'mAs', font=("Consolas",25), bg="black", fg = "black")
# 		mAlabel.place(x=850, y= 230)
# 		mAlabel = Label(root, text='mA', font=("Consolas",30), bg="black", fg = "black")
# 		mAlabel.place(x=850, y= 230)
# 		textosg = Text(root)
# 		textosg.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "black") 
# 		textosg.insert(INSERT, sg )
# 		textosg.place(x=935 , y = 220) 
# 		sglabel = Label(root, text=sin_seg, font=("Consolas",25), bg="black", fg = "black")
# 		sglabel.place(x=1055, y= 230)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_sens1 = Button(root, image = imagen_sens1, width = 80, height = 50, command = sensibilidad1)
# 		boton_sens1.place(x=110 , y = 50)
# 		boton_sens2 = Button(root, image = imagen_sens2 , width = 80, height = 50, command = sensibilidad2)
# 		boton_sens2.place(x=110 , y = 120)
# 		boton_sens3 = Button(root, image = imagen_sens3 , width = 80, height = 50, command = sensibilidad3)
# 		boton_sens3.place(x=110 , y = 190)
# 		boton_smallman = Button(root, image = imagen_smallman , width = 80, height = 50, command = delgado_gordo)
# 		boton_smallman.place(x=1130 , y = 190)
# 		boton_bigman = Button(root, image = imagen_bigman , width = 80, height = 50, command = gordo_delgado)
# 		boton_bigman.place(x=1225 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural, command = b_mural_pressed)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,   command = directo_pressed)
# 		boton_directo.place(x=330, y = 670)
# 		boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 		boton_torax_pa.place(x=460 , y = 530)
# 		boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 		boton_torax_lat.place(x=555 , y = 530)
# 		boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 		boton_parrilla_costal.place(x=460, y = 600)
# 		boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 		boton_hombro.place(x=555 , y = 600)
# 		boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 		boton_cervical_ap.place(x=460, y = 670)
# 		boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 		boton_senos_paranasales.place(x=555 , y = 670)
# 		boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 		boton_craneo_ap_pa.place(x=460, y = 740)
# 		boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 		boton_craneo_lateral.place(x=555 , y = 740)
# 		boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 		boton_abdomen_simple.place(x=685 , y = 530)
# 		boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 		boton_cadera_femur.place(x=780 , y = 530)
# 		boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 		boton_dorsal_ap.place(x=685, y = 600)
# 		boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 		boton_dorsal_lat.place(x=780 , y = 600)
# 		boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 		boton_Lumbar_ap.place(x=685, y = 670)
# 		boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 		boton_Lumbar_lat.place(x=780 , y = 670)
# 		boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 		boton_hueso_nasal.place(x=685, y = 740)
# 		boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 		boton_sacro_lateral.place(x=780 , y = 740)
# 		boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 		boton_rodilla_ap.place(x=910 , y = 530)
# 		boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 		boton_tibia_perone.place(x=1005 , y = 530)
# 		boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 		boton_Tobillo_lateral.place(x=910, y = 600)
# 		boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 		boton_pie_ap.place(x=1005 , y = 600)
# 		boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 		boton_codo_ap_lat.place(x=910, y = 670)
# 		boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 		boton_Mano_ap_obl.place(x=1005 , y = 670)
# 		boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 		boton_dedos.place(x=910, y = 740)
# 		boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 		boton_muñecca_ap.place(x=1005 , y = 740)
# 		boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 		boton_cam1.place(x=10 , y = 50)
# 		boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 		boton_cam2.place(x=10 , y = 120)
# 		boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 		boton_cam3.place(x=10 , y = 190)
# 		boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = muñeca_ap)
# 		boton_b_mesa.place(x=235 , y = 600)
# 		boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural,    command = muñeca_ap)
# 		boton_b_mural.place(x=235, y = 670)
# 		boton_directo = Button(root,  width = 80, height = 50,image = directo,    command = muñeca_ap)
# 		boton_directo.place(x=330, y = 670)
# 		boton_kv_mas = Button(root, text = "kV-mAs" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mAs)
# 		boton_kv_mas.place(x=10 , y = 260)
# 		boton_kv_mas_s = Button(root, text = "kV-mA-s" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mA_sg)
# 		boton_kv_mas_s.place(x=110 , y = 260)


			

# 	def encender():	
# 		focos1=Label(root, image=ff, width=100	, height=42)
# 		focos1.place(x=280 , y =230)
# 		telefono_label = Label(root, image=telefono, bg="black")
# 		telefono_label.place(x=250 , y =120)
# 		alarm_display_label = Label(root, image=alarm_display)
# 		alarm_display_label.place(x=300 , y =120)
# 		ready_label = Label(root, image=ready, bg="black")
# 		ready_label.place(x=350 , y =120)

# 		textokv = Text(root)
# 		textokv.config( width=3, height=1, font=("Consolas",40), bg="black", fg = "red") 
# 		textokv.insert(INSERT, kv )
# 		textokv.place(x=505 , y = 220) 
# 		kvlabel = Label(root, text="KV", font=("Consolas",25), bg="black", fg = "red")
# 		kvlabel.place(x=600, y= 230)
# 		textomA = Text(root)
# 		textomA.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "red") 
# 		textomA.insert(INSERT, mA)
# 		textomA.place(x=730 , y = 220) 
# 		mAlabel = Label(root, text='mA', font=("Consolas",25), bg="black", fg = "red")
# 		mAlabel.place(x=850, y= 230)
# 		textosg = Text(root)
# 		textosg.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "red") 
# 		textosg.insert(INSERT, sg )
# 		textosg.place(x=935 , y = 220) 
# 		sglabel = Label(root, text=sin_seg, font=("Consolas",25), bg="black", fg = "red")
# 		sglabel.place(x=1055, y= 230)
# 		telefono_label = Label(root, image=black, bg="black")
# 		telefono_label.place(x=250 , y =120)
# 		alarm_display_label = Label(root, image=black)
# 		alarm_display_label.place(x=300 , y =120)

# 	root = Toplevel()
	
# 	ancho_ventana = 1325
# 	alto_ventana = 850


# 	x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
# 	y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

# 	posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana-90)
# 	root.geometry(posicion)

# 	root.resizable(0,0)
# 	# root.geometry("1325x850")
# 	# root.resizable(0,0)
# 	root.title("                                                                                                                             SIMULADOR CONSOLA MEDIO CP PHILIPS REALIZADO POR XRAY SERVICE SOLUTIONS")
# 	root.iconbitmap('C:/master_python/xray_ide/Consola1ph/xray.ico')

# 	imagen_ff = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/imagen_ff.png')
# 	imagen_fg = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/imagen_fg.png')
# 	imagen_cam1 = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/cam1.png')
# 	imagen_cam2 = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/cam2.png')
# 	imagen_cam3 = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/cam3.png')
# 	imagen_cam1_yellow = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/cam1yellow.png')
# 	imagen_cam2_yellow = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/cam2yellow.png')
# 	imagen_cam3_yellow = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/cam3yellow.png')



# 	imagen_sens1 = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/sens1.png')
# 	imagen_sens2 = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/sens2.png')
# 	imagen_sens3 = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/sens3.png')
# 	imagen_sens1_yellow = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/sens1_yellow.png')
# 	imagen_sens2_yellow = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/sens2_yellow.png')
# 	imagen_sens3_yellow = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/sens3_yellow.png')
# 	imagen_shoot = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/simbolorx.png')
# 	imagen_alarm = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/alarm.png')
# 	imagen_smallman = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/smallman.png')
# 	imagen_bigman = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/bigman.png')
# 	imagen_smallman_yellow = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/smallman_yellow.png')
# 	imagen_bigman_yellow = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/bigman_yellow.png')
# 	b_mesa = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/b_mesa.png')
# 	b_mural = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/b_mural.png')
# 	directo = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/directo.png')
# 	b_mesa_yellow = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/b_mesa_yellow.png')
# 	b_mural_yellow = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/b_mural_yellow.png')
# 	directo_yellow = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/directo_yellow.png')
# 	on = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/on.png')
# 	off = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/off.png')
# 	shoot = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/disparo.png')
# 	black = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/black.png')
# 	ff = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/ff.png')
# 	fg = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/fg.png')
# 	ready = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/ready.png')
# 	alarm_display = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/alarm_display.png')
# 	telefono = PhotoImage(file='C:/master_python/xray_ide/Consola1ph/telefono.png')





# 	frame_display = Frame(root, width = 885 , height = 200 , bg = "black") 
# 	frame_display.place (x=220 , y =100)
# 	focos1=Label(root, image=ff, width=100	, height=42)
# 	focos1.place(x=280 , y =230)
# 	boton_ff = Button(root , width = 80, height = 50, image = imagen_ff, command = foco_fino)
# 	boton_ff.place(x=235 , y = 320)
# 	boton_fg = Button(root,  width = 80, height = 50, image = imagen_fg,  command = foco_grueso)
# 	boton_fg.place(x=330, y = 320)
# 	telefono_label = Label(root, image=black, bg="black")
# 	telefono_label.place(x=250 , y =120)
# 	alarm_display_label = Label(root, image=black)
# 	alarm_display_label.place(x=300 , y =120)
# 	ready_label = Label(root, image=ready, bg="black")
# 	ready_label.place(x=350 , y =120)

# 	textokv = Text(root)
# 	textokv.config( width=3, height=1, font=("Consolas",40), bg="black", fg = "red") 
# 	textokv.insert(INSERT, skv )
# 	textokv.place(x=505 , y = 220) 
# 	kvlabel = Label(root, text="KV", font=("Consolas",25), bg="black", fg = "red")
# 	kvlabel.place(x=600, y= 230)
# 	boton_bajarkv = Button(root, text = "-" , width = 5, height = 1,bg ="white", font=("Consolas",20))
# 	boton_bajarkv.place(x=460 , y = 320)
# 	boton_bajarkv.bind('<Button-1>', lambda e: Thread(target=click_kv_cont_down, daemon=True).start())
# 	boton_bajarkv.bind('<ButtonRelease-1>', release_kv_cont_down)
# 	boton_subirkv = Button(root, text = "+", width = 5, height = 1,bg ="white", font=("Consolas",20))
# 	boton_subirkv.place(x=555, y = 320)
# 	boton_subirkv.bind('<Button-1>', lambda e: Thread(target=click_kv_cont_up, daemon=True).start())
# 	boton_subirkv.bind('<ButtonRelease-1>', release_kv_cont_up)

# 	textomA = Text(root)
# 	textomA.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "red") 
# 	textomA.insert(INSERT, smA)
# 	textomA.place(x=730 , y = 220) 
# 	mAlabel = Label(root, text='mA', font=("Consolas",25), bg="black", fg = "red")
# 	mAlabel.place(x=850, y= 230)

# 	boton_bajarmA = Button(root, text = "-" , width =5, height = 1,bg ="white", font=("Consolas",20), command = mAdown)
# 	boton_bajarmA.place(x=685 , y = 320)
# 	boton_subirmA = Button(root, text = "+", width = 5, height = 1,bg ="white", font=("Consolas",20),  command = mAup)
# 	boton_subirmA.place(x=780, y = 320)

# 	textosg = Text(root)
# 	textosg.config( width=4, height=1, font=("Consolas",40), bg="black", fg = "red") 
# 	textosg.insert(INSERT, ssg )
# 	textosg.place(x=935 , y = 220) 
# 	sglabel = Label(root, text=ssin_seg, font=("Consolas",25), bg="black", fg = "red")
# 	sglabel.place(x=1055, y= 230)
# 	boton_bajarsg = Button(root, text = "-" , width = 5, height = 1,bg ="white", font=("Consolas",20), command = sgdown)
# 	boton_bajarsg.place(x=910 , y = 320)
# 	boton_subirsg = Button(root, text = "+", width = 5, height = 1,bg ="white", font=("Consolas",20),  command = sgup)
# 	boton_subirsg.place(x=1005, y = 320)
# 	boton_cam1 = Button(root, image = imagen_cam1 , width = 80, height = 50, command = cam1_pressed)
# 	boton_cam1.place(x=10 , y = 50)
# 	boton_cam2 = Button(root, image = imagen_cam2 , width = 80, height = 50, command = cam2_pressed)
# 	boton_cam2.place(x=10 , y = 120)
# 	boton_cam3 = Button(root, image = imagen_cam3 , width = 80, height = 50, command = cam3_pressed)
# 	boton_cam3.place(x=10 , y = 190)
# 	boton_kv_mas = Button(root, text = "kV-mAs" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mAs)
# 	boton_kv_mas.place(x=10 , y = 260)

# 	boton_sens1 = Button(root, image = imagen_sens1 , width = 80, height = 50, command = sensibilidad1)
# 	boton_sens1.place(x=110 , y = 50)
# 	boton_sens2 = Button(root, image = imagen_sens2 , width = 80, height = 50, command = sensibilidad2)
# 	boton_sens2.place(x=110 , y = 120)
# 	boton_sens3 = Button(root, image = imagen_sens3 , width = 80, height = 50, command = sensibilidad3)
# 	boton_sens3.place(x=110 , y = 190)
# 	boton_kv_mas_s = Button(root, text = "kV-mA-s" , width = 11, height = 3, font=("Consolas",10),bg ="white", command = kv_mA_sg)
# 	boton_kv_mas_s.place(x=110 , y = 260)

# 	boton_reset = Button(root, text = "Reset" , width = 11, height = 3, bg ="white", command = reset)
# 	boton_reset.place(x=1130 , y = 50)
# 	boton_alarm = Button(root, image = imagen_alarm , width = 80, height = 50, command = alarm_off)
# 	boton_alarm.place(x=1225 , y = 50)
# 	boton_smallman = Button(root, image = imagen_smallman , width = 80, height = 50, command = delgado_gordo)
# 	boton_smallman.place(x=1130 , y = 190)
# 	boton_bigman = Button(root, image = imagen_bigman , width = 80, height = 50, command = gordo_delgado)
# 	boton_bigman.place(x=1225 , y = 190)

# 	boton_b_mesa = Button(root , width = 80, height = 50, image = b_mesa, command = b_mesa_pressed)
# 	boton_b_mesa.place(x=235 , y = 600)
# 	boton_libre1 = Button(root,  width = 11, height = 3, bg ="white",  command = sgup)
# 	boton_libre1.place(x=330, y = 600)
# 	boton_b_mural = Button(root,  width = 80, height = 50, image = b_mural, bg ="white",   command = b_mural_pressed)
# 	boton_b_mural.place(x=235, y = 670)
# 	boton_directo = Button(root,  width = 80, height = 50,image = directo, bg ="white",   command = directo_pressed)
# 	boton_directo.place(x=330, y = 670)
# 	boton_libre2 = Button(root,  width = 11, height = 3, bg ="white",   command = sgup)
# 	boton_libre2.place(x=235, y = 740)
# 	boton_libre3 = Button(root,  width = 11, height = 3, bg ="white",   command = sgup)
# 	boton_libre3.place(x=330, y = 740)

# 	boton_torax_pa = Button(root , width = 11, height = 3, text = "Torax p.a.",bg ="white", command = to_pa)
# 	boton_torax_pa.place(x=460 , y = 530)
# 	boton_torax_lat = Button(root , width = 11, height = 3, text = "Torax lat",bg ="white", command = to_lat)
# 	boton_torax_lat.place(x=555 , y = 530)
# 	boton_parrilla_costal = Button(root , width = 11, height = 3, text = "Parrilla costal",bg ="white", command = pa_cost)
# 	boton_parrilla_costal.place(x=460, y = 600)
# 	boton_hombro = Button(root , width = 11, height = 3, text = "Hombro",bg ="white", command = hombro)
# 	boton_hombro.place(x=555 , y = 600)
# 	boton_cervical_ap = Button(root , width = 11, height = 3, text = "Cervical a.p.",bg ="white", command = cerv_ap)
# 	boton_cervical_ap.place(x=460, y = 670)
# 	boton_senos_paranasales = Button(root , width = 11, height = 3, text = "S. paranasales",bg ="white", command = s_paran)
# 	boton_senos_paranasales.place(x=555 , y = 670)
# 	boton_craneo_ap_pa = Button(root , width = 11, height = 3, text = "Cráneo ap-pa",bg ="white", command = craneo_ap)
# 	boton_craneo_ap_pa.place(x=460, y = 740)
# 	boton_craneo_lateral = Button(root , width = 11, height = 3, text = "Cráneo lateral",bg ="white", command = craneo_lat)
# 	boton_craneo_lateral.place(x=555 , y = 740)

# 	boton_abdomen_simple = Button(root , width = 11, height = 3, text = "Abdomen sim.",bg ="white", command = abd_simple)
# 	boton_abdomen_simple.place(x=685 , y = 530)
# 	boton_cadera_femur = Button(root , width = 11, height = 3, text = "Cadera Femur",bg ="white", command = cadera_femur)
# 	boton_cadera_femur.place(x=780 , y = 530)
# 	boton_dorsal_ap = Button(root , width = 11, height = 3, text = "Dorsal a.p.",bg ="white", command = dorsal_ap)
# 	boton_dorsal_ap.place(x=685, y = 600)
# 	boton_dorsal_lat = Button(root , width = 11, height = 3, text = "Dorsal lateral",bg ="white", command = dorsal_lat)
# 	boton_dorsal_lat.place(x=780 , y = 600)
# 	boton_Lumbar_ap = Button(root , width = 11, height = 3, text = "Lumbar a.p.",bg ="white", command = lumbar_ap)
# 	boton_Lumbar_ap.place(x=685, y = 670)
# 	boton_Lumbar_lat = Button(root , width = 11, height = 3, text = "Lumbar lateral",bg ="white", command = lumbar_lat)
# 	boton_Lumbar_lat.place(x=780 , y = 670)
# 	boton_hueso_nasal = Button(root , width = 11, height = 3, text = "Hueso nasal",bg ="white", command = hueso_nasal)
# 	boton_hueso_nasal.place(x=685, y = 740)
# 	boton_sacro_lateral = Button(root , width = 11, height = 3, text = "Sacro lateral",bg ="white", command = sacro_lat)
# 	boton_sacro_lateral.place(x=780 , y = 740)

# 	boton_rodilla_ap = Button(root , width = 11, height = 3, text = "Rodilla a.p.",bg ="white", command = rodilla_ap)
# 	boton_rodilla_ap.place(x=910 , y = 530)
# 	boton_tibia_perone = Button(root , width = 11, height = 3, text = "Tibia/perone",bg ="white", command = tibia_perone)
# 	boton_tibia_perone.place(x=1005 , y = 530)
# 	boton_Tobillo_lateral = Button(root , width = 11, height = 3, text = "Tobillo lat.",bg ="white", command = tobillo_lat)
# 	boton_Tobillo_lateral.place(x=910, y = 600)
# 	boton_pie_ap = Button(root , width = 11, height = 3, text = "Pie a.p.",bg ="white", command = pie_ap)
# 	boton_pie_ap.place(x=1005 , y = 600)
# 	boton_codo_ap_lat = Button(root , width = 11, height = 3, text = "Codo ap/lat",bg ="white", command = codo_ap_lat)
# 	boton_codo_ap_lat.place(x=910, y = 670)
# 	boton_Mano_ap_obl = Button(root , width = 11, height = 3, text = "Mano ap/obl",bg ="white", command = mano_ap_obl)
# 	boton_Mano_ap_obl.place(x=1005 , y = 670)
# 	boton_dedos = Button(root , width = 11, height = 3, text = "Dedos",bg ="white", command = dedos)
# 	boton_dedos.place(x=910, y = 740)
# 	boton_muñecca_ap = Button(root , width = 11, height = 3, text = "Muñeca a.p.",bg ="white", command = muñeca_ap)
# 	boton_muñecca_ap.place(x=1005 , y = 740)

# 	boton_on = Button(root , width = 80, height = 50, image = on, command = encender)
# 	boton_on.place(x=10 , y = 600)
# 	boton_off = Button(root , width = 160, height = 50, image = off, command = apagar)
# 	boton_off.place(x=10 , y = 740)
# 	boton_shoot = Button(root , width = 50, height = 50, image = shoot)
# 	boton_shoot.place(x=1177 , y = 740)
# 	boton_shoot.bind('<Button-1>', lambda e: Thread(target=click_shoot, daemon=True).start())
# 	boton_shoot.bind('<ButtonRelease-1>', release_shoot)
# 	splabel = Label(root, text="  ", font=("Consolas",25), bg="grey", fg = "red")
# 	splabel.place(x=1120, y= 745)
# 	splabel = Label(root, text="  ", font=("Consolas",25), bg="grey", fg = "red")
# 	splabel.place(x=1250, y= 745)

# 	root.mainloop()







