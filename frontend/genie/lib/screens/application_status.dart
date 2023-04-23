import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';
import 'package:genie/utils/colors.dart';
import 'package:timeline_tile/timeline_tile.dart';

class ApplicationStatus extends StatefulWidget {
  const ApplicationStatus({super.key});

  @override
  State<ApplicationStatus> createState() => _ApplicationStatusState();
}

class _ApplicationStatusState extends State<ApplicationStatus> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: mobileBackgroundColor,
        leading: IconButton(
          icon: const Icon(
            Icons.arrow_back,
            color: secondaryColor,
          ),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 10),
        child: Column(
          children: [
            TimelineTile(
              isFirst: true,
              endChild: Text(
                "ROhan Bera",
              ),
            ),
            TimelineTile(
              endChild: Text("Bera"),
            ),
            TimelineTile(
              endChild: Text("Bera"),
            ),
            TimelineTile(
              endChild: Text("Bera"),
            ),
            TimelineTile(
              endChild: Text("Bera"),
            ),
          ],
        ),
      ),
    );
  }
}
