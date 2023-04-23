import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';
import 'package:flutter_svg/svg.dart';
import 'package:genie/screens/application_status.dart';
import 'package:genie/screens/inbox.dart';
import 'package:genie/screens/lets_get_wishing.dart';

import '../utils/colors.dart';

class Profile extends StatelessWidget {
  const Profile({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: mobileBackgroundColor,
        centerTitle: false,
        title: SvgPicture.asset(
          "assets/logo.svg",
          color: blueColor,
          height: 32,
        ),
        actions: [
          IconButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const Inbox()),
              );
            },
            icon: Icon(
              Icons.messenger_outline,
              color: yellowColor,
            ),
          ),
        ],
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          child: Container(
            width: double.infinity,
            decoration: BoxDecoration(
              color: whiteColor,
            ),
            child: Column(
              // crossAxisAlignment: CrossAxisAlignment.end,
              children: [
                Container(
                  height: 256,
                  color: blueColor,
                  child: Center(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Container(
                          width: 128,
                          height: 128,
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(64),
                            image: DecorationImage(
                              fit: BoxFit.cover,
                              image: NetworkImage(
                                  "https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=772&q=80"),
                            ),
                          ),
                        ),
                        Container(
                          // margin: EdgeInsets.fromLTRB(1, 0, 0, 0),
                          child: Text(
                            'Ashley , 29',
                            textAlign: TextAlign.center,
                            style: TextStyle(
                              fontSize: 15,
                              fontWeight: FontWeight.w500,
                              color: whiteColor,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                Container(
                  padding: EdgeInsets.all(20),
                  width: double.infinity,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      Container(
                        padding: EdgeInsets.all(20),
                        width: double.infinity,
                        decoration: BoxDecoration(
                          color: Color(0xffeeeeee),
                          borderRadius: BorderRadius.circular(15),
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Container(
                              margin: EdgeInsets.fromLTRB(0, 0, 0, 20),
                              width: double.infinity,
                              child: Row(
                                crossAxisAlignment: CrossAxisAlignment.center,
                                children: [
                                  CircleAvatar(
                                    radius: 20,
                                    backgroundImage:
                                        AssetImage("assets/signup.jpeg"),
                                  ),
                                  SizedBox(
                                    width: 10,
                                  ),
                                  Container(
                                    // aboutmeCTD (513:5126)
                                    margin: EdgeInsets.fromLTRB(0, 0, 0, 0.2),
                                    child: Text(
                                      'About me',
                                      style: TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.w700,
                                        color: Color(0xff150b3d),
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            Container(
                              child: Text(
                                'Hi I’m Ashley! I’m a proud mother to a strong, brave young boy named Andy! If you have any questions regarding wish process please let me know!',
                                style: TextStyle(
                                  fontSize: 14,
                                  fontWeight: FontWeight.w400,
                                  color: Color(0xff514a6b),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                      SizedBox(
                        height: 10,
                      ),
                      Container(
                        padding: EdgeInsets.all(20),
                        width: double.infinity,
                        decoration: BoxDecoration(
                          color: Color(0xffeeeeee),
                          borderRadius: BorderRadius.circular(15),
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Container(
                              // autogroupkxuyiro (SQSJGS36uLW4veudpBKxuy)
                              width: double.infinity,
                              child: Row(
                                crossAxisAlignment: CrossAxisAlignment.center,
                                children: [
                                  Container(
                                    // chH (513:5127)
                                    margin: EdgeInsets.fromLTRB(0, 0, 16.97, 0),
                                    child: Text(
                                      '📍',
                                      style: TextStyle(
                                        fontSize: 24,
                                        fontWeight: FontWeight.w700,
                                        color: Color(0xff000000),
                                      ),
                                    ),
                                  ),
                                  Container(
                                    // locationJKD (513:5116)
                                    margin: EdgeInsets.fromLTRB(0, 0, 0, 3.98),
                                    child: Text(
                                      'Location',
                                      style: TextStyle(
                                        fontSize: 16,
                                        fontWeight: FontWeight.w700,
                                        color: primaryColor,
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            Text(
                              // sanfranciscocaAsD (513:5114)
                              'San Francisco, CA',
                              style: TextStyle(
                                fontSize: 16,
                                fontWeight: FontWeight.w700,
                                height: 1.3025,
                                color: Color(0xff150b3d),
                              ),
                            ),
                          ],
                        ),
                      ),
                      GestureDetector(
                        onTap: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => const GetWishing()),
                          );
                        },
                        child: Padding(
                          padding: const EdgeInsets.fromLTRB(40, 20, 40, 10),
                          child: Container(
                            height: 50,
                            decoration: BoxDecoration(
                              color: lightBlueColor,
                              borderRadius: BorderRadius.circular(30),
                            ),
                            child: Center(
                              child: Text(
                                'TALK TO A COORDINATOR',
                                style: TextStyle(
                                  fontSize: 15,
                                  fontWeight: FontWeight.w500,
                                  color: whiteColor,
                                ),
                              ),
                            ),
                          ),
                        ),
                      ),
                      GestureDetector(
                        onTap: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => const ApplicationStatus(),
                            ),
                          );
                        },
                        child: Padding(
                          padding: const EdgeInsets.fromLTRB(40, 0, 40, 10),
                          child: Container(
                            height: 50,
                            decoration: BoxDecoration(
                              color: lightBlueColor,
                              borderRadius: BorderRadius.circular(30),
                            ),
                            child: Center(
                              child: Text(
                                'REQUEST A WISH',
                                style: TextStyle(
                                  fontSize: 15,
                                  fontWeight: FontWeight.w500,
                                  color: whiteColor,
                                ),
                              ),
                            ),
                          ),
                        ),
                      ),
                      GestureDetector(
                        onTap: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => const ApplicationStatus(),
                            ),
                          );
                        },
                        child: Padding(
                          padding: const EdgeInsets.fromLTRB(40, 0, 40, 10),
                          child: Container(
                            height: 50,
                            decoration: BoxDecoration(
                              color: lightBlueColor,
                              borderRadius: BorderRadius.circular(30),
                            ),
                            child: Center(
                              child: Text(
                                'APPLICATION STATUS',
                                style: TextStyle(
                                  fontSize: 15,
                                  fontWeight: FontWeight.w500,
                                  color: whiteColor,
                                ),
                              ),
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
