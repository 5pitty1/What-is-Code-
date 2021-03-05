//
//  ContentView.swift
//  Rocky Papery Scissors
//
//  Created by Michael Remediakis on 3/10/20.
//  Copyright © 2020 Mikeyopolis. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    var moveOptions = ["Rock", "Paper", "Scissors"]
    
    @State private var playerScore = 0

    @State private var shouldWin = Bool.random()
    @State private var appMove = Int.random(in: 0..<3)
    
    var body: some View {
        VStack(spacing: 30) {
            Text("Player Score: \(playerScore)")

            Text("My move is \(moveOptions[appMove])")
            
            if shouldWin {
                Text("Try to beat me.")
            } else {
                Text("Try to lose against me")
            }
            
            ForEach(0..<3) { number in
                Button(action: {
                    self.chosenMove(number)
                }) {
                    Text(self.moveOptions[number])
                }
            }
            
        }
    }
    
    func chosenMove(_ number: Int) {
        if number == (appMove + 1) % 3 {
            playerScore += shouldWin ? 1 : 0
        } else {
            playerScore += shouldWin ? 0 : 1
        }
        
        shouldWin = Bool.random()
        appMove = Int.random(in: 0..<3)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
