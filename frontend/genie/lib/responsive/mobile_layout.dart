import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';
import 'package:genie/utils/colors.dart';
import 'package:genie/utils/global_vars.dart';

class MobileLayout extends StatefulWidget {
  const MobileLayout({super.key});

  @override
  State<MobileLayout> createState() => _MobileLayoutState();
}

class _MobileLayoutState extends State<MobileLayout> {
  int _page = 0;
  late PageController pageController;

  @override
  void initState() {
    super.initState();
    pageController = PageController();
  }

  @override
  void dispose() {
    super.dispose();
    pageController.dispose();
  }

  void navigationTapped(int page) {
    pageController.jumpToPage(page);
  }

  void onPageChanged(int page) {
    setState(() {
      _page = page;
    });
  }

  @override
  Widget build(BuildContext context) {
    // return CupertinoTabScaffold(
    //     tabBar: CupertinoTabBar(items: [
    //       BottomNavigationBarItem(
    //         icon: Icon(
    //           Icons.home,
    //           color: _page == 0 ? yellowColor : secondaryColor,
    //         ),
    //         label: '',
    //         backgroundColor: primaryColor,
    //       ),
    //       BottomNavigationBarItem(
    //         icon: Icon(
    //           Icons.search,
    //           color: _page == 1 ? yellowColor : secondaryColor,
    //         ),
    //         label: '',
    //         backgroundColor: primaryColor,
    //       ),
    //       BottomNavigationBarItem(
    //         icon: Container(
    //           padding: EdgeInsets.symmetric(
    //             horizontal: 20,
    //             vertical: 8,
    //           ),
    //           decoration: BoxDecoration(
    //             color: redColor,
    //             borderRadius: BorderRadius.all(
    //               Radius.circular(20),
    //             ),
    //           ),
    //           child: Icon(
    //             color: _page == 2 ? yellowColor : whiteColor,
    //             Icons.add,
    //           ),
    //         ),
    //         label: '',
    //         backgroundColor: primaryColor,
    //       ),
    //       BottomNavigationBarItem(
    //         icon: Icon(
    //           Icons.star,
    //           color: _page == 3 ? yellowColor : secondaryColor,
    //         ),
    //         label: '',
    //         backgroundColor: primaryColor,
    //       ),
    //       BottomNavigationBarItem(
    //         icon: Icon(
    //           Icons.person,
    //           color: _page == 4 ? yellowColor : secondaryColor,
    //         ),
    //         label: '',
    //         backgroundColor: primaryColor,
    //       )
    //     ]),
    //     tabBuilder: (context, index) {
    //       return CupertinoTabView(builder: (context) {
    //         return CupertinoPageScaffold(
    //           child: homeScreenItems[index],
    //         );
    //       });
    //     });

    return Scaffold(
      backgroundColor: mobileBackgroundColor,
      body: PageView(
        children: homeScreenItems,
        controller: pageController,
        onPageChanged: onPageChanged,
      ),
      bottomNavigationBar: CupertinoTabBar(
        height: 60,
        iconSize: 20,
        backgroundColor: mobileBackgroundColor,
        border: const Border(
            top: BorderSide(color: mobileBackgroundColor, width: 0)),
        items: [
          BottomNavigationBarItem(
            icon: Icon(
              Icons.home,
              color: _page == 0 ? yellowColor : secondaryColor,
            ),
            label: '',
            backgroundColor: primaryColor,
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.search,
              color: _page == 1 ? yellowColor : secondaryColor,
            ),
            label: '',
            backgroundColor: primaryColor,
          ),
          BottomNavigationBarItem(
            icon: Container(
              padding: EdgeInsets.symmetric(
                horizontal: 20,
                vertical: 8,
              ),
              decoration: BoxDecoration(
                color: redColor,
                borderRadius: BorderRadius.all(
                  Radius.circular(20),
                ),
              ),
              child: Icon(
                color: _page == 2 ? yellowColor : whiteColor,
                Icons.add,
              ),
            ),
            label: '',
            backgroundColor: primaryColor,
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.star,
              color: _page == 3 ? yellowColor : secondaryColor,
            ),
            label: '',
            backgroundColor: primaryColor,
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.person,
              color: _page == 4 ? yellowColor : secondaryColor,
            ),
            label: '',
            backgroundColor: primaryColor,
          )
        ],
        onTap: navigationTapped,
      ),
    );
  }
}
