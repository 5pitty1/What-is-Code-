//
//  ContentView.swift
//  MatheMagic
//
//  Created by Michael Remediakis on 4/5/20.
//  Copyright © 2020 Mikeyopolis. All rights reserved.
//

import SwiftUI

class UserSettings: ObservableObject {
    @Published var multiplicationTable = 9
    @Published var numQuestions = 0
    @Published var gameRunning = false
    
    let numQuestionsChoices = ["5", "10", "20", "All"]
}

struct UserSettingsView: View {
    @ObservedObject var settings:UserSettings
    
    var body: some View {
        NavigationView {
            VStack {
                Form {
                    Section {
                        Text("Choose a multiplication table").font(.headline)
                        
                        Stepper(value: $settings.multiplicationTable, in: 3...12) {
                            Text("\(settings.multiplicationTable)x\(settings.multiplicationTable)")
                        }
                    }
                    
                    Section {
                        Text("How many questions do you want to be asked?").font(.headline)
                        
                        Picker(selection: $settings.numQuestions, label: Text("How many questions do you want to be asked?")) {
                            ForEach(0 ..< settings.numQuestionsChoices.count) {
                                Text(self.settings.numQuestionsChoices[$0])
                            }
                        }.pickerStyle(SegmentedPickerStyle())
                    }
                }.navigationBarTitle(Text("Mathemagic!"))
                
                Button(action: {
                    withAnimation {
                        self.settings.gameRunning.toggle()
                    }
                }) {
                    Text("Start Game")
                }
            }
        }
    }
}

struct GameplayView: View {
    var settings:UserSettings
    var questions:[(question:String, answer:Int)]
    
    init(settings:UserSettings) {
        self.settings = settings
        questions = []
        for i in 1...settings.multiplicationTable {
            for j in 1...settings.multiplicationTable {
                questions.append(("\(i)x\(j)", i*j))
            }
        }
        questions.shuffle()
    }
    
    var allQuestions:Int {
        self.settings.multiplicationTable * self.settings.multiplicationTable
    }
    
    var numQuestions:Int {
        let i = self.settings.numQuestions
        let numQuestions = self.settings.numQuestionsChoices[i]
        
        return min(Int(numQuestions) ?? allQuestions, allQuestions)
    }
    
    @State private var currentQuestion = 0
    @State private var userAnswer = ""
    @State private var questionColor = Color.blue
    
    var body: some View {
        ZStack {
            self.questionColor.edgesIgnoringSafeArea(.all)
            VStack(spacing: 20) {
                Text("\(questions[currentQuestion].question)")
                    .font(.system(size: 60))
                    .frame(width: 240, height: 140)
                    .background(Color.white)
                    .cornerRadius(10)
                
                if currentQuestion < numQuestions {
                    HStack(spacing: 0) {
                        TextField("Answer", text: $userAnswer)
                            .keyboardType(.numberPad)
                            .font(.title)
                            .padding(10)
                            .frame(width: 140, height: 40)
                            .background(Color.white)
                        
                        Button(action: {
                            let answerInt = Int(self.userAnswer) ?? 0
                            
                            if answerInt == self.questions[self.currentQuestion].answer {
                                withAnimation(.linear(duration:0.3)) {
                                    self.questionColor = Color.blue
                                }
                            } else {
                                withAnimation(.linear(duration:0.3)) {
                                    self.questionColor = Color.red
                                }
                            }

                            self.currentQuestion += 1

                        }) {
                            Text("Go")
                                .foregroundColor(Color.white)
                                .font(.system(size: 20))
                        }
                        .frame(width: 40, height: 40)
                        .background(Color.green)

                        
                    }
                    .cornerRadius(10)
                } else {
                    Button(action: {
                        withAnimation {
                            self.settings.gameRunning.toggle()
                        }
                    }) {
                        Text("Start Over")
                            .foregroundColor(Color.white)
                            .font(.system(size: 20))
                    }
                    .frame(width: 180, height: 40)
                    .background(Color.green)
                    .cornerRadius(10)

                }
            }
        }
    }
}

struct ContentView: View {
    
    @ObservedObject var userSettings:UserSettings = UserSettings()
    
    var body: some View {
        Group {
            if userSettings.gameRunning {
                GameplayView(settings: userSettings)
            } else {
                UserSettingsView(settings: userSettings)
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
