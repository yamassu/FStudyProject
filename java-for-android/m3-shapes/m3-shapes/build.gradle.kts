plugins {
    alias(libs.plugins.android.application) apply false
}

tasks.register("clean", Delete::class) {
    delete(layout.buildDirectory.get())
}

if (file("$projectDir/gradle/tools.gradle").exists()) {
    apply(from = "$projectDir/gradle/tools.gradle")
}
