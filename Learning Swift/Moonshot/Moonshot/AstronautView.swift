//
//  AstronautView.swift
//  Moonshot
//
//  Created by Michael Remediakis on 5/1/20.
//  Copyright © 2020 Mikeyopolis. All rights reserved.
//

import SwiftUI

struct AstronautView: View {
    let astronaut: Astronaut
    let missions: [Mission]
    
    var body: some View {
        GeometryReader { geometry in
            ScrollView(.vertical) {
                VStack {
                    Image(self.astronaut.id)
                        .resizable()
                        .scaledToFit()
                        .frame(width: geometry.size.width)
                    
                    Text(self.astronaut.description)
                        .padding()
                        .layoutPriority(1)
                    
                    Text("Missions")
                        .font(.headline)

                    List(self.missions) { mission in
                            Text(mission.displayName)
                    }
                    
                }
            }
        }
        .navigationBarTitle(Text(astronaut.name), displayMode: .inline)
    }
    
    init(astronaut:Astronaut) {
        self.astronaut = astronaut
        
        let missions: [Mission] = Bundle.main.decode("missions.json")
        
        self.missions = missions.filter { mission in
            return mission.crew.contains(where: { $0.name == astronaut.id})
        }
        
    }
}

struct AstronautView_Previews: PreviewProvider {
    static let astro: [Astronaut] = Bundle.main.decode("astronauts.json")
    static var previews: some View {
        AstronautView(astronaut: astro[0])
    }
}
