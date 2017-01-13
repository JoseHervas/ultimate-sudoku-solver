from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import sudoku
from solver.sudoku_solver import *

def solution(request, input_sudoku):
	solution = solve(input_sudoku)
	order = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','B1','B2','B3','B4','B5','B6','B7','B8','B9','C1','C2','C3','C4','C5','C6','C7','C8','C9','D1','D2','D3','D4','D5','D6','D7','D8','D9','E1','E2','E3','E4','E5','E6','E7','E8','E9','F1','F2','F3','F4','F5','F6','F7','F8','F9','G1','G2','G3','G4','G5','G6','G7','G8','G9','H1','H2','H3','H4','H5','H6','H7','H8','H9','I1','I2','I3','I4','I5','I6','I7','I8','I9']
	return render(request, 'solver/templates/solution.html', {'solution': solution, 'order':order})

def home(request):
	if request.method == 'POST':
		form = sudoku(request.POST)
		if form.is_valid():
			raw_data = form.cleaned_data
			return HttpResponseRedirect('/' + str(raw_data['A1']) + str(raw_data['A2']) + str(raw_data['A3']) + str(raw_data['A4']) + str(raw_data['A5']) + str(raw_data['A6']) + str(raw_data['A7']) + str(raw_data['A8']) + str(raw_data['A9']) + str(raw_data['B1']) + str(raw_data['B2']) + str(raw_data['B3']) + str(raw_data['B4']) + str(raw_data['B5']) + str(raw_data['B6']) + str(raw_data['B7']) + str(raw_data['B8']) + str(raw_data['B9']) + str(raw_data['C1']) + str(raw_data['C2']) + str(raw_data['C3']) + str(raw_data['C4']) + str(raw_data['C5']) + str(raw_data['C6']) + str(raw_data['C7']) + str(raw_data['C8']) + str(raw_data['C9']) + str(raw_data['D1']) + str(raw_data['D2']) + str(raw_data['D3']) + str(raw_data['D4']) + str(raw_data['D5']) + str(raw_data['D6']) + str(raw_data['D7']) + str(raw_data['D8']) + str(raw_data['D9']) + str(raw_data['E1']) + str(raw_data['E2']) + str(raw_data['E3']) + str(raw_data['E4']) + str(raw_data['E5']) + str(raw_data['E6']) + str(raw_data['E7']) + str(raw_data['E8']) + str(raw_data['E9']) + str(raw_data['F1']) + str(raw_data['F2']) + str(raw_data['F3']) + str(raw_data['F4']) + str(raw_data['F5']) + str(raw_data['F6']) + str(raw_data['F7']) + str(raw_data['F8']) + str(raw_data['F9']) + str(raw_data['G1']) + str(raw_data['G2']) + str(raw_data['G3']) + str(raw_data['G4']) + str(raw_data['G5']) + str(raw_data['G6']) + str(raw_data['G7']) + str(raw_data['G8']) + str(raw_data['G9']) + str(raw_data['H1']) + str(raw_data['H2']) + str(raw_data['H3']) + str(raw_data['H4']) + str(raw_data['H5']) + str(raw_data['H6']) + str(raw_data['H7']) + str(raw_data['H8']) + str(raw_data['H9']) + str(raw_data['I1']) + str(raw_data['I2']) + str(raw_data['I3']) + str(raw_data['I4']) + str(raw_data['I5']) + str(raw_data['I6']) + str(raw_data['I7']) + str(raw_data['I8']) + str(raw_data['I9']))
	else:
		form = sudoku()
	return render(request, 'solver/templates/home.html', {'form': form})