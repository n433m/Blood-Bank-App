#!/usr/bin/python3

class BloodDonator:

	donator_count=0

	bloodbank = {
		"AB+":{},
		"AB-":{},
		"A+":{},
		"B+":{},
		"B-":{},
		"O+":{},
		"O-":{}
	}


	def __init__(self):
		pass



	def entry_exists(self, b_group, name, area, phone, last_donate):
		details = [name, phone, last_donate]

		if area in BloodDonator.bloodbank[b_group].keys():

			for item in BloodDonator.bloodbank[b_group][area]:
				if item == details:
					return True

		return False




	def delete_entry(self, b_group, name, area, phone, last_donate):
		details = [name, phone, last_donate]

		self.flag = False
		self.found = False

		if area in BloodDonator.bloodbank[b_group].keys():

			for item in BloodDonator.bloodbank[b_group][area]:
				if item == details:
					self.found = True
					BloodDonator.bloodbank[b_group][area].remove(item)
					self.flag = True

			if self.flag == True:
				print("Deleted.")
				
		if self.found is False:
			print("Entry doesn't exist!")
		


	def add_new_donater(self, b_group, name, area, phone, last_donate):
		BloodDonator.donator_count += 1
		details = [name, phone, last_donate]

		if BloodDonator.entry_exists(self, b_group, name, area, phone, last_donate) is True:
			print("Entry exists!")
			return

		if area in BloodDonator.bloodbank[b_group].keys():
			BloodDonator.bloodbank[b_group][area].append(details)
		elif area not in BloodDonator.bloodbank[b_group].keys():
			BloodDonator.bloodbank[b_group][area] = [details]


	def search_blood(self, b_group, area):
		if area in BloodDonator.bloodbank[b_group].keys():
			return BloodDonator.bloodbank[b_group][area]
		else:
			print("No donator Exists!")
			return
	def show_list(self, b_group, area):
		infolist = BloodDonator.search_blood(self, b_group, area)

		try:
			for item in infolist:
				print("Name : {name}  Phone No-{phone}  Last Donate-{date}".format(name=item[0], phone=item[1], date=item[2]))
		except TypeError:
			pass



if __name__ == '__main__':

	donation_archive = BloodDonator()

	while(True):
		print(
			"""
			Choose Option
			1. Search
			2. Add Donator
			3. Delete Donator
			4. Exit

			"""
			)

		option = int(input())

		if option == 1:
			b_group = input("Blood Group: ")
			area = input("Area: ")
			donation_archive.show_list(b_group, area)
			continue

		elif option == 2:
			op = int(input("Press 1 to add or 0 to back: "))
			if op == 0:
				continue
			else:
				name = input("Name: ")
				b_group = input("Blood Group: ")
				area = input("Area: ")
				phone = input("Phone Number: ")
				last_donate = input("Last Donate Date(day-month-year): ")

				donation_archive.add_new_donater(b_group, name, area, phone, last_donate)
				continue

		elif option == 3:
			op = int(input("Press 1 to delete or 0 to back"))
			if op == 0:
				continue
			else:
				name = input("Name: ")
				b_group = input("Blood Group: ")
				area = input("Area: ")
				phone = input("Phone Number: ")
				last_donate = input("Last Donate Date(day-month-year): ")

				donation_archive.delete_entry(b_group, name, area, phone, last_donate)
				continue

		elif option == 4:
			break

