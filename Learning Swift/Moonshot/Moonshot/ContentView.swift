//
//  ContentView.swift
//  Moonshot
//
//  Created by Michael Remediakis on 4/20/20.
//  Copyright © 2020 Mikeyopolis. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    let astronauts:[Astronaut] = Bundle.main.decode("astronauts.json")
    let missions:[Mission] = Bundle.main.decode("missions.json")
    @State private var showingMissions = true
    
    var body: some View {
        NavigationView {
            if showingMissions {
                List(missions) { mission in
                    MissionListItem(mission: mission, astronauts: self.astronauts)
                }
                .navigationBarTitle("Moonshot")
                .navigationBarItems(trailing: Button("Crew") {
                    self.showingMissions.toggle()
                })

            } else {
                List(astronauts) { astronaut in
                    AstronautListItem(astronaut: astronaut)
                }
                .navigationBarTitle("Moonshot")
                .navigationBarItems(trailing: Button("Missions") {
                    self.showingMissions.toggle()
                })

            }
        }
    }
}

struct MissionListItem: View {
    let mission: Mission
    let astronauts: [Astronaut]
    
    var body: some View {
        NavigationLink(destination: MissionView(mission: mission, astronauts: astronauts)) {
            Image(mission.image)
                .resizable()
                .scaledToFit()
                .frame(width: 44, height: 44)
            
            VStack(alignment: .leading) {
                Text(mission.displayName)
                    .font(.headline)
                Text(mission.formattedLaunchDate)
            }
        }
    }
}

struct AstronautListItem: View {
    let astronaut: Astronaut
    
    var body: some View {
        NavigationLink(destination: AstronautView(astronaut: astronaut)) {
            Image(astronaut.id)
                .resizable()
                .scaledToFit()
                .frame(width: 44, height: 44)
                .clipShape(Circle())
            
            Text(astronaut.name)
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
