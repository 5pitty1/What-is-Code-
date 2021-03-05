//
//  ContentView.swift
//  GuessTheFlag
//
//  Created by Michael Remediakis on 3/4/20.
//  Copyright © 2020 Mikeyopolis. All rights reserved.
//

import SwiftUI

struct FlagImage: View {
    var country: String
    
    var body: some View {
        Image(country)
        .renderingMode(.original)
        .clipShape(Capsule())
        .overlay(Capsule().stroke(Color.black, lineWidth: 1))
            .shadow(color: .black, radius: 2)
    }
}

struct ContentView: View {
    @State private var countries = ["Estonia", "France", "Germany", "Ireland", "Italy", "Nigeria", "Poland", "Russia", "Spain", "UK", "US"].shuffled()
    @State private var correctAnswer = Int.random(in: 0...2)
    @State private var userGuess = 0
    
    @State private var userScore = 0
    @State private var showingScore = false
    @State private var scoreTitle = ""
    
    @State private var rotations:[Double] = [0, 0, 0]
    @State private var opacities:[Double] = [1, 1, 1]

    var body: some View {
        ZStack {
            LinearGradient(gradient: Gradient(colors: [.blue, .black]), startPoint: .top, endPoint: .bottom).edgesIgnoringSafeArea(.all)
            
            VStack(spacing: 30) {
                VStack {
                    Text("Tap the flag of")
                        .foregroundColor(.white)
                    Text(countries[correctAnswer])
                        .foregroundColor(.white)
                        .font(.largeTitle)
                        .fontWeight(.black)
                }
                
                ForEach(0..<3) { number in
                    Button(action: {
                        self.flagTapped(number)
                    }) {
                        FlagImage(country: self.countries[number])
                    }
                    .rotation3DEffect(.degrees(self.rotations[number]), axis: (x:0,y:1,z:0))
                    .opacity(self.opacities[number])
                }
                
                Text("Score: \(userScore)")
                    .foregroundColor(.white)
            }
        }
        .alert(isPresented: $showingScore) {
            if userGuess == correctAnswer{
                return Alert(title: Text(scoreTitle), message: Text("Your score is \(userScore)"), dismissButton: .default(Text("Continue")) {
                        self.askQuestion()
                    })
            } else {
                return Alert(title: Text(scoreTitle), message: Text("Wrong! That's the flag of \(countries[userGuess])"), dismissButton: .destructive(Text("Continue")))
            }
        }
    }
    
    func flagTapped(_ number: Int) {
        if number == correctAnswer {
            withAnimation {
                self.rotations[number] += 360
                self.opacities[(number + 1) % 3] = 0.2
                self.opacities[(number + 2) % 3] = 0.2
            }
            scoreTitle = "Correct"
            userScore += 1
        } else {
            withAnimation {
                self.opacities[number] = 0
            }
            scoreTitle = "Wrong"
        }
        
        userGuess = number
        showingScore = true
    }
    
    func askQuestion() {
        countries.shuffle()
        withAnimation {
            for i in 0..<3 {
                opacities[i] = 1
            }
        }
        correctAnswer = Int.random(in: 0..<2)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
