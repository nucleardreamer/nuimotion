{
  "variables": {
    "OPENNI2%": "$(OPENNI2)",
    "NITE2%": "$(NITE2)"
  },
  "targets": [
    {
	    "target_name": "copy-files",
      "conditions": [
        [
          "OS=='linux'",
          {
            "copies": [
              {
                "files": [
                  "<(OPENNI2)/Drivers/libOniFile.so",
                  "<(OPENNI2)/Drivers/libPS1080.so",
                  "<(OPENNI2)/Drivers/PS1080.ini",
                  "<(OPENNI2)/Drivers/PSLink.ini"
                ],
                "destination": "<(module_root_dir)/build/Release/OpenNI2/Drivers/"
              },
              {
                "files": [
                  "<(NITE2)/Data/lbsdata.idx",
                  "<(NITE2)/Data/lbsdata.lbd",
                  "<(NITE2)/Data/lbsparam1.lbd",
                  "<(NITE2)/Data/lbsparam2.lbd"
                ],
                "destination": "<(module_root_dir)/../../NiTE2/Data/"
              },
              {
                "files": [
                  "<(NITE2)/FeatureExtraction.ini",
                  "<(NITE2)/h.dat",
                  "<(NITE2)/HandAlgorithms.ini",
                  "<(NITE2)/s.dat"
                ],
                "destination": "<(module_root_dir)/../../NiTE2/"
              },
              {
                "files": [
                  "</usr/lib/libOpenNI2.so",
                  "</etc/openni2/OpenNI.ini",
                  "<(NITE2)/Redist/libNiTE2.so",
                  "<(NITE2)/Redist/NiTE.ini"
                ],
                "destination": "<(module_root_dir)/build/Release/"
              }
            ]
          }
        ]
      ]
    },
    {
      "target_name": "nuimotion",
      "sources": [
        "src/Main.cpp",
        "src/enums/EnumMapping.cpp",
        "src/gestures/GestureRecognizer.cpp",
        "src/gestures/Swipe.cpp",
        "src/gestures/Wave.cpp"
      ],
      "conditions": [
        [
          "OS=='linux'",
          {
            "libraries": [
              "/usr/lib/libOpenNI2.so",
              "<(NITE2)/Redist/libNiTE2.so"
            ]
          }
        ]
      ],
      "include_dirs": [
        "./src/enums",
        "./build/Release",
        "<(OPENNI2)/Include/",
        "<(NITE2)/Include/"
      ]
    },
    {
      "target_name": "nuimotion-depth",
      "sources": [
        "src/Depth.cpp",
        "src/enums/EnumMapping.cpp",
        "src/gestures/GestureRecognizer.cpp",
        "src/gestures/Swipe.cpp",
        "src/gestures/Wave.cpp"
      ],
      "conditions": [
        [
          "OS=='linux'",
          {
            "libraries": [
              "<(OPENNI2)/Tools/libOpenNI2.so"
            ]
          }
        ]
      ],
      "include_dirs": [
        "<(OPENNI2)/Include/"
      ]
    }
  ]
}
