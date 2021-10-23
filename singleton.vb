Module Singlton

    Class Singleton
        Private Shared _instance As Singleton
        Protected Sub New()
        End Sub

        Public Shared Function Instance() As Singleton
            If _instance Is Nothing Then
                _instance = New Singleton()
            End If
            Return _instance
        End Function
    End Class

    Class MainApp
        Public Shared Sub Main()
            Dim s1 As Singleton = Singleton.Instance()
            Dim s2 As Singleton = Singleton.Instance()

            If s1 Is s2 Then
                Console.WriteLine("Objects are the same instance")
            End If

        End Sub
    End Class

End Module
