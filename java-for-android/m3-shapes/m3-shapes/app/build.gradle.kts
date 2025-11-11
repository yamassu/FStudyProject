import org.gradle.api.tasks.testing.logging.TestExceptionFormat

plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
}

android {
    namespace = project.properties["project.namespace"] as String

    compileSdk = libs.versions.compileSdk.get().toInt()

    defaultConfig {
        applicationId = "com.example.app"
        minSdk = libs.versions.minSdk.get().toInt()
        targetSdk = libs.versions.targetSdk.get().toInt()
        versionCode = libs.versions.versionCode.get().toInt()
        versionName = libs.versions.versionName.get()

    }

    buildTypes {
        getByName("release") {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android.txt"),
                "proguard-rules.pro"
            )
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }
    kotlinOptions {
        jvmTarget = "11"
    }

    buildFeatures {
        buildConfig = true
    }

    @Suppress("UnstableApiUsage")
    testOptions {
        unitTests.apply {
            isIncludeAndroidResources = true
            isReturnDefaultValues = true
        }
    }

    packaging {
        resources.excludes += setOf(
            "META-INF/LICENSE.txt",
            "META-INF/NOTICE.txt"
        )
    }
}

tasks.withType<Test> {
    testLogging {
        ignoreFailures = true
        maxHeapSize = "1024m"
        events("passed", "skipped", "failed")
        outputs.upToDateWhen { false }
        showStandardStreams = true
        showExceptions = true
        showStackTraces = true
        showCauses = true
        exceptionFormat = TestExceptionFormat.FULL
    }
}

dependencies {
    implementation(
        fileTree(mapOf("dir" to "libs", "include" to listOf("*.jar")))
    )
    implementation(libs.bundles.androidCore)
    implementation(libs.guava)
    testImplementation(libs.bundles.testing)
}
